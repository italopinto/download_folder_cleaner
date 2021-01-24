# Scripts em python para automatizar a "limpeza" do diretório de downloads do Ubuntu Linux 20.10

* **Créditos:** Ao Jhonatan da [Dev Aprender](https://www.devaprender.com), autor desse projeto.

# Projeto
* O projeto consiste em automatizar a organização do diretório Downloads, inicialmente, foi feito para windows, pelo autor original. Meu fork foi para adaptar os scripts ao meu Ubuntu Linux 20.10.
* Foram feitas algumas modificações, por exemplo, tive que mudar apenas os caminhos para o diretório, pois o sistema de arquivos das distribuições linux, são diferentes do windows.
* Porém a maior mudança consistiu em criar um arquivo de log, pois como o intuito é pôr esse script para rodar como um serviço do sistema, em background, as mensagens não poderiam ser exibidas no terminal, portanto, com o uso do módulo python **logging**, todas as mensagens ficarão salvas em log.
* Há um arquivo de teste para mover um arquivo específico ou fazer download de um vídeo direto do youtube usano o módulo [pytube](https://pypi.org/project/pytube/). Modifique de acordo com suas necessidades.
