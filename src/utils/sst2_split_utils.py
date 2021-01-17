import argparse
import csv
import logging

import os

import sys

TRAINID = 1
TESTID = 2
DEVID = 3


class SST2SplitUtils:
    """
    The SST2 utils for splitting data into train , test and validation
    """

    def __init__(self):
        pass

    def split(self, input_file, split_file: str, dictionary: str, label_file: str, output_dir):

        splits = self._load_splits(split_file)
        dictionary_phrase_map = self._load_dictionary(dictionary)
        phrase_sentiment = self._load_phrase_sentiments(label_file)

        train, dev, test = self._load_sentences_with_sentiment(input_file, dictionary_phrase_map,
                                                               phrase_sentiment, splits)

        self._write_csv(train, os.path.join(output_dir, "train.csv"))
        self._write_csv(dev, os.path.join(output_dir, "dev.csv"))
        self._write_csv(test, os.path.join(output_dir, "test.csv"))

    @property
    def _logger(self):
        return logging.getLogger(__name__)

    def _load_sentences_with_sentiment(self, raw_input_file, dictionary_phrase_map, phrase_sentiment, splits):
        train, dev, test = [], [], []
        id_data_map = {
            TRAINID: train,
            TESTID: dev,
            DEVID: test
        }
        missing_sen = 0
        total_sen = 0
        with open(raw_input_file, "r", encoding="utf-8") as f:
            for l in f.readlines()[1:]:
                total_sen += 1
                sentence_id, text = l.split("\t")[0], "\t".join(l.split("\t")[1:]).rstrip("\n")
                sentence_id = int(sentence_id)
                split_id = splits[sentence_id]
                if text not in dictionary_phrase_map:
                    self._logger.warning("Text not found in dictionary: {}".format(text))
                    missing_sen += 1
                    continue
                phrase_id = dictionary_phrase_map[text]
                id_data_map[split_id].append({"text": text, "label": phrase_sentiment[phrase_id]})

            self._logger.warning("A {} out of {} were not found in dictionary".format(missing_sen, total_sen))

        return id_data_map[TRAINID], id_data_map[DEVID], id_data_map[TESTID]

    def _load_phrase_sentiments(self, label_file):
        phrase_sentiment = {}
        sep = "|"
        with open(label_file, "r") as f:
            for l in f.readlines()[1:]:
                phrase_id, confidence = l.split(sep)[0], l.split(sep)[1].rstrip("\n")
                phrase_id = int(phrase_id)

                phrase_sentiment[phrase_id] = self._get_sentiment(float(confidence))

        return phrase_sentiment

    def _get_sentiment(self, confidence):
        """
        Return sentiment given confidence
        :param confidence:
        :return:
        """
        # Confidence intervals
        # [0, 0.2], (0.2, 0.4], (0.4, 0.6], (0.6, 0.8], (0.8, 1.0]
        if 0 <= confidence <= 0.4: return "Negative"
        if 0.4 < confidence <= 0.6: return "Neutral"
        if 0.6 < confidence <= 1.0: return "Positive"

    def _load_splits(self, split_file):
        splits = {}

        with open(split_file, "r") as f:
            for l in f.readlines()[1:]:
                sentence_id, split_id = l.split(",")[0], l.split(",")[1].rstrip("\n")
                sentence_id = int(sentence_id)
                splits[sentence_id] = int(split_id)

        return splits

    def _load_dictionary(self, dictionary_file):
        dictionary_phrase_map = {}
        with open(dictionary_file, "r", encoding="utf-8") as f:
            for l in f.readlines()[1:]:
                text, phrase_id = l.split("|")[0], l.split("|")[1].rstrip("\n")
                phrase_id = int(phrase_id)
                dictionary_phrase_map[text] = int(phrase_id)

        return dictionary_phrase_map

    def _write_csv(self, data, output_file):
        self._logger.info("Writing to {}".format(output_file))
        with open(output_file, "w") as f:
            csv_writer = csv.writer(f, delimiter='\t',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for r in data:
                csv_writer.writerow([r["text"], r["label"]])


def run_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sentencefile",
                        help="The input sentence file, e.g. datasetSentences.txt ", required=True)
    parser.add_argument("--sentiment",
                        help="The sentiment file, e.g. sentiment_labels.txt ", required=True)
    parser.add_argument("--dictionary",
                        help="The dictionary file, dictionary.txt", required=True)
    parser.add_argument("--split",
                        help="The split file, e.g. datasetSplit.txt ", required=True)
    parser.add_argument("--outdir",
                        help="The output directory to write files to ", required=True)
    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})
    args = parser.parse_args()
    print(args.__dict__)
    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    os.makedirs(args.outdir, exist_ok=True)

    SST2SplitUtils().split(args.sentencefile, args.split, args.dictionary, args.sentiment, args.outdir)


if __name__ == "__main__":
    run_main()
