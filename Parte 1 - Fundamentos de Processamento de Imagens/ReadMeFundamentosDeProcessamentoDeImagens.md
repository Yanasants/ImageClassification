RESUMO

O primeiro arquivo corresponde a um código que trabalha os Fundamentos de Processamento de Imagens Digitais,
explorando as dimensões das imagens bem como a sua representação matricial e as transformações a serem aplicadas
para garantir os processamentos das imagens em si. São utilizadas duas imagens, uma em preto e branco (não originalmente, mas com o parâmetro as_gray ativo) denominada "pct.png", e duas coloridas, denominadas "ufopa0.png" e "flash.PNG". Dessa forma, são 
trabalhados a) remodelagem dos arrays correspondentes às imagens, b) extração de recursos de borda das imagens digitais.

BIBLIOTECAS

- Pandas;
- Numpy;
- Matploblib;
- Skimage.

DESENVOLVIMENTO

Para a imagem "pct.png":

- Verificação da dimensionalidade;
- Transformação do array bidimensional ao unidimensional.

Para a imagem "ufopa0.png":

- Verificação da dimensionalidade;
- Criação de um array de mesma dimensão preenchido por zeros;
- Acréscimo do valor médio dos canais (3 canais, RBG) no array criado;
- Transformação do array bidimensional ao unidimensional;

Para a imagem "flash.PNG":

- Verificação das bordas das imagens através das funções PREWITT, que comparam os valores de pixels vizinhos.

REFERÊNCIAS

MENESES, Anderson. Introdução a Fundamentos de Processamento Digital de Imagens. Apresentação de Power Point. 104 slides. color.

SINGH, Aishwarya. Beginner Beginner-Friendly Techniques to Extract Features from
Image Data using Python. Analytics Vidhya, 2019. Disponível em: <https://www.analyticsvidhya.com/blog/2019/08/3-techniques-extract-features-from-image-data-machine-learning-python/>. Acesso em: 10 de Novembro de 2021.

PARA MAIS INFORMAÇÕES TEÓRICAS:
https://drive.google.com/file/d/1NZ2pSrqLGgxMaUQB8rPMGVRnIsJgXomI/view?usp=sharing