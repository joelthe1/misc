## Hidden Markov Model based Automatic Morphological Tagger
### What does this do?
Tries to automatically learn the morphological tags from a tagged training data set and attempts to assign tags to a given set of untagged sentences (test data).


### Training Data Format
Βίβλος/N-NSF γενέσεως/N-GSF Ἰησοῦ/N-GSM Χριστοῦ/N-GSM υἱοῦ/N-GSM Δαυείδ/N-PRI υἱοῦ/N-GSM Ἀβραάμ/N-PRI  
Πᾶσαι/A-NPF οὖν/CONJ αἱ/T-NPF γενεαί/N-NPF ἀπό/PREP Ἀβραάμ/N-PRI ἕως/ADV Δαυείδ/N-PRI γενεαί/N-NPF δεκατέσσαρες/A-NPF καί/CONJ ἀπό/PREP Δαυείδ/N-PRI ἕως/ADV τῆς/T-GSF μετοικεσίας/N-GSF Βαβυλῶνος/N-GSF γενεαί/N-NPF δεκατέσσαρες/A-NPF καί/CONJ ἀπό/PREP τῆς/T-GSF μετοικεσίας/N-GSF Βαβυλῶνος/N-GSF ἕως/ADV τοῦ/T-GSM Χριστοῦ/N-GSM γενεαί/N-NPF δεκατέσσαρες/A-NPF  
...  
...  


### Test Data Format
Παῦλος ἀπόστολος Χριστοῦ Ἰησοῦ διά θελήματος Θεοῦ τοῖς ἁγίοις τοῖς οὖσιν ἐν Ἐφέσῳ καί πιστοῖς ἐν Χριστῷ Ἰησοῦ χάρις ὑμῖν καί εἰρήνη ἀπό Θεοῦ Πατρός ἡμῶν καί Κυρίου Ἰησοῦ Χριστοῦ  
τῇ γάρ χάριτι ἐστε σεσῳσμένοι διά πίστεως καί τοῦτο οὐκ ἐξ ὑμῶν Θεοῦ τό δῶρον οὐκ ἐξ ἔργων ἵνα μή τις καυχήσηται  
αὐτοῦ γάρ ἐσμεν ποίημα κτισθέντες ἐν Χριστῷ Ἰησοῦ ἐπί ἔργοις ἀγαθοῖς οἷς προητοίμασεν ὁ Θεός ἵνα ἐν αὐτοῖς περιπατήσωμεν  
...  
...  


### Output Format
Παῦλος/N-NSM ἀπόστολος/N-NSM Χριστοῦ/N-GSM Ἰησοῦ/N-GSM διά/PREP θελήματος/N-GSN Θεοῦ/N-GSM τοῖς/T-DPM ἁγίοις/A-DPM τοῖς/T-DPM οὖσιν/V-PAP-DPM ἐν/PREP Ἐφέσῳ/N-DSF καί/CONJ πιστοῖς/A-DPM ἐν/PREP Χριστῷ/N-DSM Ἰησοῦ/N-DSM χάρις/N-NSF ὑμῖν/P-2DP καί/CONJ εἰρήνη/N-NSF ἀπό/PREP Θεοῦ/N-GSM Πατρός/N-GSM ἡμῶν/P-1GP καί/CONJ Κυρίου/N-GSM Ἰησοῦ/N-GSM Χριστοῦ/N-GSM  
τῇ/T-DSF γάρ/CONJ χάριτι/N-DSF ἐστε/V-PAI-2P σεσῳσμένοι/CONJ διά/PREP πίστεως/N-GSF καί/CONJ τοῦτο/D-ASN οὐκ/PRT-N ἐξ/PREP ὑμῶν/P-2GP Θεοῦ/N-GSM τό/T-ASN δῶρον/N-ASN οὐκ/PRT-N ἐξ/PREP ἔργων/N-GPN ἵνα/CONJ μή/PRT-N τις/X-NSM καυχήσηται/V-ADS-3S  
αὐτοῦ/P-GSM γάρ/CONJ ἐσμεν/V-PAI-1P ποίημα/T-ASM κτισθέντες/N-ASM ἐν/PREP Χριστῷ/N-DSM Ἰησοῦ/N-DSM ἐπί/PREP ἔργοις/N-DPN ἀγαθοῖς/A-DPN οἷς/R-DPN προητοίμασεν/V-AAI-3S ὁ/T-NSM Θεός/N-NSM ἵνα/CONJ ἐν/PREP αὐτοῖς/P-DPM περιπατήσωμεν/V-AAS-1P  
...  
...  
