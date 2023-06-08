# LMFlow Benchmark

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_es.md">Español</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_jp.md">日本語</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_ko.md">한국어</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_hindi.md">हिंदी</a>
    <p>
</h4>

[![Website](https://img.shields.io/badge/Website-Demo-20B2AA.svg)](https://lmflow.com)
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/Discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-Join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.imgloc.com/2023/06/01/Vki1CZ.jpeg)

This project provides a unified framework to evaluation generative large language models on different evaluation tasks.

Large Model for All. See our [vision](https://github.com/OptimalScale/LMFlow#vision).

## Latest News
* [2023-05-08] :rocket: Release [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), an automatic evaluation framework for open-source chat-style LLMs. [Benchmark results](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0) on 31 popular models are reported. [Participate in LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:

## Supported Models

Seamlessly supported all the [decoder models](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads) in 🤗 Hugging Face. 
LLaMA, GPT2, GPT-Neo, Galactica, have been fully tested. We will support encoder models soon.

## 1.Setup

Our package has been fully tested on Linux OS (Ubuntu 20.04). Other OS platforms (MacOS, Windows) are not fully tested.
You may encounter some unexpected errors. You may try it first on a Linux machine or use Google Colab to experience it.

```bash
git clone https://github.com/research4pan/lmflow-benchmark.git
cd lmflow-benchmark
conda create -n lmflow-benchmark python=3.9 -y
conda activate lmflow-benchmark
pip install -e .
```

## 2.Prepare Dataset

Please refer to our [doc](https://optimalscale.github.io/LMFlow/examples/DATASETS.html).

## 3. Running Scripts
### 3.1 LMFlow Benchmark
LMFlow Benchmark is an automatic evaluation framework for open-source large language models.
We use negative log likelihood (NLL) as the metric to evaluate different aspects of a language model: chitchat, commonsense reasoning, and instruction following abilities.

You can directly run the LMFlow benchmark evaluation to obtain the results to participate in the
[LLM comparision](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit?usp=sharing).
For example, to run GPT2 XL, one may execute
```sh
./scripts/run_benchmark.sh --model_name_or_path gpt2-xl
```
`--model_name_or_path` is required, you may fill in huggingface model name or local model path here.

To check the evaluation results, you may check `benchmark.log` in `./output_dir/gpt2-xl_lmflow_chat_nll_eval`,
`./output_dir/gpt2-xl_all_nll_eval` and `./output_dir/gpt2-xl_commonsense_qa_eval`.

## Vision
Make evaluation of LLMs automatic, Hello there! We are excited to announce the upcoming release of our code repository that includes a complete LLM training process, enabling users to quickly build their own language models and train them effectively.

Our code repository is not just a simple model; it includes the complete training workflow, model optimization, and testing tools. You can use it to build various types of language models, including conversation models, question-answering models, and text generation models, among others.

Moreover, we aim to create an open and democratic LLM sharing platform where people can share their checkpoints and experiences to collectively improve the skills of the community. We welcome anyone who is interested in LLM to participate and join us in building an open and friendly community!

Whether you are a beginner or an expert, we believe that you can benefit from this platform. Let's work together to build a vibrant and innovative LLM community!

[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.imgloc.com/2023/06/01/Vki1CZ.jpeg)

## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
If you find this repository useful, please consider giving ⭐ and citing:

```
@misc{lmflow,
  author = {Shizhe Diao and Rui Pan and Hanze Dong and KaShun Shum and Jipeng Zhang and Wei Xiong and Tong Zhang},
  title = {LMFlow: An Extensible Toolkit for Finetuning and Inference of Large Foundation Models},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://optimalscale.github.io/LMFlow/}},
}
```
