# MSMS-BLAST
## Using Protein Localization Studies to Assess the GeTRPRA Framework*

### Project abstract
- Towards the improvement of human genome-scale metabolic models (GEMs), it is important to consider the biological roles of protein isoforms in the context of human metabolism. A systemic framework of gene-transcript-protein-reaction associations (GeTPRA) was developed to facilitate model integration with transcript-level compatible data characterizing the functional roles of protein isoforms. A potential problem associated with the generation of the GeTPRA framework is its employment of a prediction algorithm to obtain subcellular protein localization data. This study aims to assess the reliability of the subcellular localization data to provide suggestions for future updates of the GeTPRA framework and for the development and reconstruction of more robust human GEMs. Our analysis of protein localization information of a total of 17275 peptide sequences from two tandem mass spectrometry-based experimental datasets demonstrates that there are approximately equal proportions of GeTPRA protein localization predictions supported or not supported by experimental evidence. This result implies that more caution needs to be taken with the use of prediction algorithms alone when integrating protein localization data in the existing metabolic models. It is therefore necessary to review a substantial number of protein localization studies and to employ a hierarchical decision-making model based on reliability scores of such studies for the future improvements of the GeTPRA frameworks as well as human GEMs.

### Materials
- The experimental data chosen in this work come from two recent studies that cover data obtained from tandem mass spectrometry technique, including a sub-cellular fractionation-based study and a biotinylation study aimed at inner mitochondrial membrane (IMM) proteome using an in situ-generated radical probe with genetically targeted peroxidase (APEX) (accessed Feb 11, 2019).
#####  Links to the publications:
- https://www.ncbi.nlm.nih.gov/pubmed/28435121
- https://pubs-acs-org.proxy3.library.mcgill.ca/doi/suppl/10.1021/jacs.6b10418

### Methods
- *inputFastaGenerator.py*: to fetch and process the experimental data from the two studies aforementioned. Repeated entries of peptide sequence-subcellular location were removed, since the relative quantity of each peptide in its subcellular compartment is irrelevant in this work. The resulted list of unique peptide sequence-subcellular location entries was then used to write a FASTA file to make queries using command line BLASTP10, 11. Data from Lee et al.’s study was processed in a similar manner, with a FASTA file containing unique peptide sequences as input to command line BLASTP.
- Command line BLASTP (Version 2.8.1, build Nov 26, 2018) was run on a MacOS version 10.14.1 machine with the following parameters: evalue 100, outfmt 510, 11. The E-value cutoff was set to 100 because many of the peptide sequences obtained from the experimental studies are relatively short (Table S1). 
- *peptide_seq_length_counter.py*: to summarize the peptide length information (Table S1).
- *runblast.sh*: to streamline the process of creating a BLASTP database using the Ensembl database of all protein sequences in human genome12 (release 95, accessed Jan 26, 2019), inputting the query FASTA files to BLASTP against all peptide sequences in the Ensembl library12, and generating BLASTP output in xml format.
- *MSMS_blast_parser.py*: to process BLASTP output. The parsed output is converted into a csv file containing the following hit information for each query peptide sequence: Ensembl Gene (ENSG) ID, Ensembl Transcript (ENST) ID, Gene Name, Match Sequence, Subject Sequence, Alignment Length, Identities, E Value. 
- *entry_counter.py*: to look at the number of ENSTs and ENSGs that were mapped to three subcellular locations based on tandem mass spectrometry evidence (Table 1). The subcellular locations being mapped to are mitochondria, nucleus and cytoplasm. Light and heavy microsome experimental data were excluded due to ambiguity and lack of consensus with respect to how these locations may correspond to the subcellular locations included in the GeTPRA framework (ER membrane, peroxisome, lysosome, Golgi apparatus), in addition to the three locations that are included. A detailed discussion on whether and how these organelles could be categorized as heavy or light microsomes is beyond the scope of this study. Furthermore, each entry in the csv file for query peptide sequences is also annotated with the subcellular location information obtained from the two experimental studies aforementioned(Table S2, Table S3). 
- *compare_with_GeTPRA.py*: to parse the GeTPRA framework with the following information extracted: Entrez gene ID, ENSG, ENST, Transcript Type, Predicted Subcellular Location, Experimental Evidence on SLs. Subsequently, the parsed BLASTP output csv files are individually processed. For each ENST ID in the GeTPRA framework, its existence in the BLASTP output files was checked and experimental SL information was appended to corresponding entry if ENST ID was present in the BLASTP output files. The output is a summary data table of comparison between the GeTPRA framework and experimental protein localization information in csv format (Table S4, Table S5).
- *check_MS_evidence.py*: (the aim was to assess the coverage of GeTPRA entries with subcellular location information supported by the tandem mass spectrometry evidence from the primary literature) to search for all entries in the GeTPRA framework that has SLs supported by experimental evidence (Table S6), and all of the unique entries, in terms of ENST, that are supported (Table S7), regardless of whether the ENSTs of the entries are covered in the two experimental studies. For all of the entries with ENSTs covered at least one of the two experimental studies, this snippet was used to collect all the entries that include mitochondria/nucleus/cytoplasm for subcellular location but are not supported by experimental evidence from either of the two studies (Table S8). The unique entries, in terms of ENSTs, that are not supported was also found using the same script (Table S9).
- *coverage_histogram_generator.py*: to generate histograms of transcript coverage per gene in the GeTPRA framework by the tandem mass spectrometry evidence, and of number of transcripts per gene in the GeTPRA framework (Figure 1, Figure 2).


*\*This work is supervised by Dr. Uri David Akavia, Biochemistry Department, McGill University. A report with detailed results, discussion and references is included in this repository. All the figures, tables and supplementary information can be found under the data summary folder.*
