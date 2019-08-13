# MSMS-BLAST
## Using Protein Localization Studies to Assess the GeTRPRA Framework*

### Project abstract
- Towards the improvement of human genome-scale metabolic models (GEMs), a systemic framework of gene-transcript-protein-reaction associations (GeTPRA) was developed to facilitate model integration with transcript-level compatible data characterizing the functional roles of protein isoforms. A potential problem associated with the generation of GeTPRA is its employment of a prediction algorithm to obtain subcellular protein localization data. 
- This study aims to assess the reliability of the subcellular localization data to provide suggestions for future updates of the GeTPRA framework and for the development and reconstruction of more robust human GEMs. Our analysis of protein localization information of a total of 17275 peptide sequences from two tandem mass spectrometry-based experimental datasets demonstrates that there are approximately equal proportions of GeTPRA protein localization predictions supported or not supported by experimental evidence. This result implies that more caution needs to be taken with the use of prediction algorithms alone when integrating protein localization data in the existing metabolic models. It is therefore necessary to review a substantial number of protein localization studies and to employ a hierarchical decision-making model based on reliability scores of such studies for the future improvements of the GeTPRA frameworks as well as human GEMs.

### Materials
- The experimental data chosen in this work come from two recent studies that cover data obtained from tandem mass spectrometry technique, including a sub-cellular fractionation-based study and a biotinylation study aimed at inner mitochondrial membrane (IMM) proteome using an in situ-generated radical probe with genetically targeted peroxidase (APEX) (accessed Feb 11, 2019).
#####  Links to the publications:
- https://www.ncbi.nlm.nih.gov/pubmed/28435121
- https://pubs-acs-org.proxy3.library.mcgill.ca/doi/suppl/10.1021/jacs.6b10418

### Methods
- *inputFastaGenerator.py*: to fetch and process the experimental data from the two studies aforementioned. Repeated entries of peptide sequence-subcellular location were removed, since the relative quantity of each peptide in its subcellular compartment is irrelevant in this work.
- *peptide_seq_length_counter.py*: to summarize the peptide length information (Table S1).
- *runblast.sh*: to streamline the process of creating a BLASTP database using the Ensembl database of all protein sequences in human genome12 (release 95, accessed Jan 26, 2019).
- *MSMS_blast_parser.py*: to process BLASTP output, parse and write to a csv file containing the following hit information for each query peptide sequence: Ensembl Gene (ENSG) ID, Ensembl Transcript (ENST) ID, Gene Name, Match Sequence, Subject Sequence, Alignment Length, Identities, E Value. 
- *entry_counter.py*: to look at the number of ENSTs and ENSGs that were mapped to three subcellular locations based on tandem mass spectrometry evidence (Table 1). 
- *compare_with_GeTPRA.py*: to parse the GeTPRA framework.
- *check_MS_evidence.py*: the aim was to assess the coverage of GeTPRA entries with subcellular location information supported by the tandem mass spectrometry evidence from the primary literature
- *coverage_histogram_generator.py*: to generate histograms of transcript coverage per gene in the GeTPRA framework by the tandem mass spectrometry evidence, and of number of transcripts per gene in the GeTPRA framework (Figure 1, Figure 2).


*\*This work is under the supervison of Dr. Uri David Akavia, Biochemistry Department, McGill University. A detailed report with  results, discussion and references is included in this repository. All the figures, tables and supplementary information can be found under the data summary folder.*
