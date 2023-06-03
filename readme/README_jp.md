<p align="center" width="100%">
<img src="../assets/logo.png" alt="LMFlow" style="width: 100%; min-width: 300px; display: block; margin: auto; background-color: transparent;">
</p>

# LMFlow

<h4 align="center">
    <p>
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/README.md">English</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_es.md">Español</a> |
        <b>日本語</b> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_ko.md">한국어</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_hindi.md">हिंदी</a>
    <p>
</h4>

日文版はChatGPTによって翻訳されました。もし間違いがあれば、contributorに修正していただけると幸いです。また、英語版と内容に差異がある場合は、英語版を優先してください。

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)

This project provides a unified framework to evaluation generative large language models on different evaluation tasks.

すべての人のための大規模言語モデル。私たちの[ビジョン](https://github.com/OptimalScale/LMFlow#vision)をご覧ください

<p align="center" width="100%">
<img src="../assets/features.png" alt="LMFlow-features" style="width: 100%; min-width: 300px; display: block; margin: auto;">
</p>


## Latest News
* [2023-05-08] :rocket: Release [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), an automatic evaluation framework for open-source chat-style LLMs. [Benchmark results](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0) on 31 popular models are reported. [Participate in LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:


## Supported Models

🤗 Hugging Faceのすべての[decoder models](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads)を完全にサポートし、LLaMA、GPT2、GPT-Neo、Galacticaを完全にテストしました。エンコーダーモデルも近日中にサポートする予定です。



## 1.Setup

私たちのパッケージはLinuxオペレーティングシステム（Ubuntu 20.04）で全面的にテストされています。その他のオペレーティングシステムプラットフォーム（MacOS、Windows）はまだ全面的にテストされていません。
予期せぬエラーが発生する可能性があります。Linuxマシンで試したり、Google Colabを使って体験したりすることができます。

```bash
git clone https://github.com/OptimalScale/LMFlow.git
cd LMFlow
conda create -n lmflow python=3.9 -y
conda activate lmflow
conda install mpi4py
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
こんにちは！ 私たちは、完全なLLMトレーニングプロセスを含むコードリポジトリの近日リリースをお知らせできることを喜んでいます。これにより、ユーザーは自分自身の言語モデルを迅速に構築し、効果的にトレーニングすることができます。

私たちのコードリポジトリは単なるモデルだけでなく、完全なトレーニングワークフロー、モデルの最適化、およびテストツールを含んでいます。会話モデル、質問応答モデル、テキスト生成モデルなど、さまざまな種類の言語モデルを構築するために使用できます。

さらに、私たちは、人々がチェックポイントや経験を共有し、コミュニティのスキルを集団で向上させることができるオープンで民主的なLLM共有プラットフォームを作成することを目指しています。LLMに興味のある人は誰でも参加し、オープンでフレンドリーなコミュニティの構築に参加することを歓迎します！

初心者でもエキスパートでも、私たちはこのプラットフォームから利益を得ることができると信じています。一緒に活気ある革新的なLLMコミュニティを築いていきましょう！

[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)

## Disclaimer
このパッケージは、大規模モデルの調整のための簡素化されたユーザーフレンドリーなパイプラインを提供することを目的としています。その機能はユーザーによって参照されることを意図しており、データと事前学習済みモデルの準備に関する責任はユーザーに完全にあります。このパッケージは、ユーザーの準備からのコンポーネントの正確性、完全性、適用性、および合法性を保証しません。ユーザーはモデルとデータの準備に関連するすべてのリスクと責任を認識し、本パッケージを利用する前に法的、商業的、および技術的なアドバイスを受ける必要があります。パイプラインは、ユーザーのデータと事前学習済みモデルの不適切な準備によって生じた直接的、間接的、特別な、付随的、または結果的な損害について責任を負いません。

私たちのチェックポイントには、英語版と中国語版の両方が含まれており、研究目的にのみ提供されています。これらのチェックポイントに含まれるトレーニングデータには、ChatGPT言語モデルから生成された結果が含まれています。これらのチェックポイントの配布や使用を商業目的で推奨または促進することはできません。これらのチェックポイントのユーザーは、正しく適切に使用されるように責任を負う必要があります。

モデルによって生成された結果は確率モデルに基づいており、このパイプラインと直接関係があるわけではありません。結果の正確性、信頼性、適用性、法的性質は、このパイプラインによって保証されるものではありません。したがって、ユーザーは結果に関連するリスクと責任を認識し、法的、商業的、技術的なアドバイスを受けてから、モデル生成の結果に依存する必要があります。このパイプラインは、ユーザーがモデル生成の結果に依存することによって生じる直接的、間接的、特別、偶発的、または結果的な損害について、一切責任を負いません。

## Support
何かお困りのことがございましたら、[Github](https://github.com/OptimalScale/LMFlow)のissueにご投稿ください。

## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
もしこのリポジトリが役立った場合は、ぜひ⭐をつけて引用してください。

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
