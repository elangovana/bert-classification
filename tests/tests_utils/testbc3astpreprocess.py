import os
from io import StringIO
from unittest import TestCase

from utils.bc3ast_preprocess import BC3ASTPreprocess


class TestBC3ASTPreprocess(TestCase):
    def test_process_handle(self):
        # Arrange
        data = """19938376	Plant Signal Behav	101291431	2009	Plant caspase-like proteases in plant.	Programmed cell death (PCD) is a genetically-controlled disassembly of the cell.
"""
        annotations = """19938376	1
"""
        expected = """Programmed cell death (PCD) is a genetically-controlled disassembly of the cell.	1	19938376\r
"""
        sut = BC3ASTPreprocess()
        output = StringIO()

        # Act
        sut.process(StringIO(data), StringIO(annotations), output)

        # Assert
        self.assertSequenceEqual(expected, output.getvalue())

    def test_process_file(self):
        # Arrange
        data = os.path.join(os.path.dirname(__file__), "sample_data", "bc3_act_all_records.tsv")
        annotations = os.path.join(os.path.dirname(__file__), "sample_data", "bc3_act_gold_standard.tsv")
        output = StringIO()
        expected = """Programmed cell death (PCD) is a genetically-controlled disassembly of the cell. In animal systems, the central core execution switch for apoptotic PCD is the activation of caspases (Cysteine-containing Aspartate-specific proteases). Accumulating evidence in recent years suggests the existence of caspase-like activity in plants and its functional involvement in various types of plant PCD, although no functional homologs of animal caspases were identified in plant genome. In this mini-review, we will cover the recent results on the existence of plant caspase-like proteases and introduce major technologies used in detecting the activation of caspase-like proteases during plant PCD.	1	19938376\r
Plants develop various ER-derived structures with specific functions. The ER body found in Arabidopsis thaliana is a spindle-shaped structure. ER bodies accumulate in epidermal cells in seedlings or are induced by wounding. The molecular mechanisms underlying the formation of the ER body remained obscure. We isolated an ER body-deficient mutant in Arabidopsis seedlings, which we termed nai2. The NAI2 gene encodes a member of a unique protein family. NAI2 localizes to the ER body and the downregulation of NAI2 elongates ER bodies and reduces their number. ER bodies specifically accumulate high levels of PYK10/BGLU23, which is a beta-glucosidase that bears an ER retention signal. Additionally, in the nai2 mutant, PYK10 protein is diffuse throughout the ER and the PYK10 protein level is reduced. These observations indicate that NAI2 is a key factor for the formation of ER bodies and for the accumulation of PYK10 in the ER bodies of Arabidopsis. We also found that BGLU18, which encodes another beta-glucosidase with an ER retention signal, is induced at the site of wounding. Immunocytochemical analysis revealed that the BGLU18 protein is exclusively localized in ER bodies formed directly at the wounding site of cotyledons. These results suggest that BGLU18 is a component of the ER body in wounded leaves of Arabidopsis.	1	19847124\r
Climbing plants have fascinated botanists since the pioneering works of Darwin and his contemporaries in the 19(th) century. Diverse plants have evolved different ways of climbing and a wide range of attachment devices and stem biomechanics to cope with the particular physical demands of life as a climber. We investigated the biomechanics of attachment in a range of climbing palms, including true rattans from Southeast Asia and the genus Desmoncus from South America. We found that hook strength and orientation is coordinated with rachis geometry and rigidity. These findings support the notion of a ratchet-type attachment mechanism and partly explain why these spiny plants are so catchy and efficient at attaching to supports.	0	19847117\r
In Arabidopsis thaliana cell suspension, abscisic acid (ABA) induces changes in cytosolic calcium concentration ([Ca(2+)](cyt)) which are the trigger for ABA-induced plasma membrane anion current activation, H(+)-ATPase inhibition, and subsequent plasma membrane depolarization. In the present study, we took advantage of this model to analyze the implication of intracellular Ca(2+) stores in ABA signal transduction through electrophysiological current measurements, cytosolic Ca(2+) activity measurements with the apoaequorin Ca(2+) reporter protein and external pH measurement. Intracellular Ca(2+) stores involvement was determined by using specific inhibitors of CICR channels: the cADP-ribose/ryanodine receptor (Br-cADPR and dantrolene) and of the inositol trisphosphate receptor (U73122). In addition experiments were performed on epidermal strips of A. thaliana leaves to monitor stomatal closure in response to ABA in presence of the same pharmacology. Our data provide evidence that ryanodine receptor and inositol trisphosphate receptor could be involved in ABA-induced (1) Ca(2+) release in the cytosol, (2) anion channel activation and H(+)-ATPase inhibition leading to plasma membrane depolarization and (3) stomatal closure. Intracellular Ca(2+) release could thus contribute to the control of early events in the ABA signal transduction pathway in A. thaliana.	1	19847112\r
Cellular carbon (C) and nitrogen (N) metabolism must be tightly coordinated to sustain optimal growth and development for plants and other cellular organisms. Furthermore, C/N balance is also critical for the ecosystem response to elevated atmospheric CO(2). Despite numerous physiological and molecular studies in C/N balance or ratio response, very few genes have been shown to play important roles in C/N balance signaling. During recent five years, exciting progress was made through genetic and genomic studies. Several DNA microarray studies have shown that more than half of the transcriptome is regulated by C, N and the C-N combination. Three genetic studies involving distinct bioassays have demonstrated that a putative nitrate transporter (NTR2.1), a putative glutamate receptor (GLR1.1) and a putative methyltransferase (OSU1) have important functions in the C/N balance response. OSU1 is identical to QUA2/TSD2 which has been implicated to act in cell wall biogenesis, indicating a link between cell wall property and the C/N balance signaling. Given that many investigations are only focused on C alone or N alone, the C/N balance bioassays and gene expression patterns are discussed to assist phenotypic characterization of C/N balance signaling. Further, re-examination of those previously reported sugar or nitrogen responsive genes in C/N balance response may be necessary to dissect the C/N signaling pathways. In addition, key components involved in C-N interactions in bacterial, yeast and animal systems and whether they are functionally conserved in plants are discussed. These rapid advances have provided the first important step towards the construction of the complex yet elegant C/N balance signaling networks in plants.	0	19820356\r
"""
        sut = BC3ASTPreprocess()

        # Act
        sut.process(data, annotations, output)

        # Assert
        self.assertSequenceEqual(expected, output.getvalue())
