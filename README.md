
# **Do VSR Models Generalize Beyond LRS3?**

This repository contains our benchmark **WildVSR**, a new test set for Visual Speech Recognition on English, refer to the paper 
[Do VSR Models Generalize Beyond LRS3?](https://arxiv.org/abs/2311.14063).


## Dataset Summary

The Lip Reading Sentences-3 (LRS3) benchmark has primarily been the focus of intense research in visual speech recognition (VSR) during the last few years. As a result, there is an increased risk of overfitting to its excessively used test set, which is only one hour duration. To alleviate this issue, we build **WildVSR**, a new VSR test set by closely following the LRS3 dataset creation processes. We then evaluate and analyse the extent to which the current VSR models generalise to the new test data. We evaluate a broad range of publicly available VSR models and find significant drops in performance on our test set, compared to their corresponding LRS3 results.


## WildVSR leaderboard:

| Method | WER (LRS3) | WER (WildVSR) |
|--------|------------|------------|
| **ASR Models**           |      |      |
| Wav2vec2.0               | 6.1  | 21.8 | 
| Whisper                  | 1.1  | 1.8  |
| **Supervised**           |      |      |
| Ma et al.                | 32.3 | 61.1 |
| Prajwal et al.           | 40.6 | 75.1 |
| Prajwal et al.           | 30.7 | 67.9 | 
| Auto-AVSR                | 19.1 | 42.7 |
| **Self-Supervised Base** |      |      |
| AV-HuBERT                | 44.0 | 74.2 |
| RAVen                    | 39.1 | 70.8 |
| AV-HuBERT                | 34.8 | 61.0 |
| **Self-Supervised Large**|      |      |
| AV-HuBERT                | 41.6 | 71.4 |
| AV-HuBERT                | 28.6 | 54.7 |
| AV-HuBERT  w/ self-training |26.9 | 52.2 |
| RAVen                       |27.8 | 54.9 |
| RAVen  w/ self-training     | 23.1 | 50.0 | 


## Downloading the data:

Data can be found at this [link](https://drive.google.com/file/d/1Ok_Oyw0NzoGHZLyffZ4n-6qBmI0IGKmc/view?usp=drive_link). The test set is structured as follows:
```bash
WildVSR/
│
├── videos/
│ ├── 00001.mp4
│ └── 00001.mp4
├── labels.json/
  ├── '00001': 'label'
│ └── '00004': 'label'
```

## Intended Use

This dataset can be used to test models for visual speech recognition for English. It's particularly useful for research and development purposes in the field of audio-visual content processing. The data can be used to assess the performance of current and future models.

## Limitations and Biases
Due to the data collection process focusing on YouTube, biases inherent to the platform may be present in the dataset. Also, while measures are taken to ensure diversity in content, the dataset might still be skewed towards certain types of content due to the filtering process.

## Ethical Considerations
The dataset only uses free-to-use content, complying with legal requirements and ensuring respect for the original content creators. However, users of the dataset should keep in mind the potential biases and limitations inherent in the dataset.

## Citation
```bash
@article{djilali2023vsr,
  title={Do VSR Models Generalize Beyond LRS3?},
  author={Djilali, Yasser Abdelaziz Dahou and Narayan, Sanath and Bihan, Eustache Le and Boussaid, Haithem and Almazrouei, Ebtessam and Debbah, Merouane},
  journal={arXiv preprint arXiv:2311.14063},
  year={2023}
}
```
