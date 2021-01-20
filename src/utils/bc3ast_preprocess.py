import argparse
import csv
import logging

import os

import sys


class BC3ASTPreprocess:
    """
    Preprocess the Biocreative 3 Article classification
    """

    @property
    def _logger(self):
        return logging.getLogger(__name__)

    def process(self, data_file_or_handler, annotations_file_or_handle, outputfile_or_handle):
        label_map = self._open_handle_wrapper(annotations_file_or_handle, "r", self._load_annotations)
        data = self._open_handle_wrapper(data_file_or_handler, "r", lambda f: self._load_data(f, label_map))
        self._open_handle_wrapper(outputfile_or_handle, "w", lambda f: self._write(data, f))

    def _open_handle_wrapper(self, handler_or_file, rw_flag, func):
        if not isinstance(handler_or_file, str): return func(handler_or_file)

        with open(handler_or_file, rw_flag) as f:
            return func(f)

    def _write(self, data, output_handle):
        self._logger.info("Writing to {}".format(output_handle))

        csv_writer = csv.writer(output_handle, delimiter='\t',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for r in data:
            csv_writer.writerow([r["abstract"], r["label"], r["id"]])

    def _load_annotations(self, annotations_handler):
        sep = "\t"
        labels_map = {}
        csv_reader = csv.reader(annotations_handler, delimiter=sep,
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line_parts in csv_reader:
            id = line_parts[0]
            label = int(line_parts[1].rstrip("\r\n"))
            labels_map[id] = label
        return labels_map

    def _load_data(self, data_handle, label_map):
        data = []
        sep = "\t"
        csv_reader = csv.reader(data_handle, delimiter=sep,
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line_parts in csv_reader:
            id = line_parts[0]
            title_text = line_parts[4]
            abstract_text = line_parts[5].rstrip("\r\n")
            data.append({"title": title_text, "abstract": abstract_text, "label": label_map[id], "id": id})
        return data


def run_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datafile",
                        help="The input sentence file, e.g. bc3_act_all_records.tsv", required=True)

    parser.add_argument("--annotationsfile",
                        help="The sentiment file, e.g. bc3_act_goldstandard.tsv", required=True)

    parser.add_argument("--outputfile",
                        help="The output file to write results to", required=True)

    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})
    args = parser.parse_args()
    print(args.__dict__)
    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    os.makedirs(os.path.dirname(args.outputfile), exist_ok=True)

    BC3ASTPreprocess().process(args.datafile, args.annotationsfile, args.outputfile)


if __name__ == "__main__":
    run_main()
