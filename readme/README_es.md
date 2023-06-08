<p align="center" width="100%">
<img src="../assets/logo.png" alt="LMFlow" style="width: 100%; min-width: 300px; display: block; margin: auto; background-color: transparent;">
</p>

# LMFlow

<h4 align="center">
    <p>
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/README.md">English</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_zh-hans.md">简体中文</a> |
        <b>Español</b> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_jp.md">日本語</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_ko.md">한국어</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_hindi.md">हिंदी</a>
    <p>
</h4>

Este proyecto proporciona un marco unificado para evaluar modelos de lenguaje generativos grandes en diferentes tareas de evaluación.

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![WeChat badge](https://img.shields.io/badge/Wechat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)


This project provides a unified framework to evaluation generative large language models on different evaluation tasks.

Modelo de Lenguaje Grande para Todos. Vea nuestra [visión](https://github.com/OptimalScale/LMFlow#vision).


<p align="center" width="100%">
<img src="../assets/features.png" alt="LMFlow-features" style="width: 100%; min-width: 300px; display: block; margin: auto;">
</p>


## Latest News
[2023-05-08] :rocket: Lanzamiento de [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), un marco de evaluación automático para LLMs (modelos de lenguaje generativos grandes) de estilo de chat de código abierto.
Se [informan](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0) los resultados de la evaluación de 31 modelos populares. [Participa en LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:


## Supported Models

Ofrecemos soporte para todos los modelos [decodificadores](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads) en 🤗 huggingface. Hemos probado completamente LLaMA, GPT2, GPT-Neo, Galactica. Pronto también ofreceremos soporte para modelos codificadores.

## 1.Setup

Nuestro paquete ya está completamente probado en el sistema operativo Linux (ubuntu 20.04). otras plataformas del sistema operativo (macos, windows) aún no han sido completamente probadas.
Puede encontrar algunos errores inesperados. Puede intentarlo primero en una máquina Linux o experimentarlo con Google colab.

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
¡Hola! ¡Estamos emocionados de anunciar el próximo lanzamiento de nuestro repositorio de código que incluye un proceso completo de entrenamiento de LLM, permitiendo a los usuarios construir rápidamente sus propios modelos de lenguaje y entrenarlos de manera efectiva!

Nuestro repositorio de código no es solo un modelo simple; incluye todo el flujo de trabajo de entrenamiento, optimización de modelo y herramientas de prueba. Puedes usarlo para construir varios tipos de modelos de lenguaje, incluyendo modelos de conversación, modelos de pregunta-respuesta y modelos de generación de texto, entre otros.

Además, nuestro objetivo es crear una plataforma abierta y democrática de intercambio de LLM donde las personas puedan compartir sus checkpoints y experiencias para mejorar colectivamente las habilidades de la comunidad. ¡Damos la bienvenida a cualquier persona interesada en LLM a participar y unirse a nosotros en la construcción de una comunidad abierta y amigable!

Ya seas principiante o experto, creemos que puedes beneficiarte de esta plataforma. ¡Trabajemos juntos para construir una comunidad vibrante e innovadora de LLM!

[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)


## Support

If you need any help, please submit a [Github](https://github.com/OptimalScale/LMFlow) issue.

## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
Si encuentras este repositorio útil, por favor considera darle ⭐ y citarlo:

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


