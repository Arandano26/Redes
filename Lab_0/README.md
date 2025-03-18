
# Punto Estrella 

Los nombres de dominio tradicionales solo permiten caracteres ASCII. Sin embargo, con el crecimiento de Internet a nivel global, surgió la necesidad de incluir nombres de dominio en otros idiomas y con caracteres especiales. Para resolver esto, se desarrollaron los **Nombres de Dominio Internacionalizados (IDN)**, que permiten el uso de caracteres Unicode. **Unicode** es un estándar que permite representar texto en cualquier idioma, incluyendo chino, árabe e incluso emojis.

Dado que los sistemas de nombres de dominio en Internet solo manejan caracteres ASCII, se utiliza un mecanismo de codificación llamado **Punycode**. Este algoritmo convierte los nombres de dominio con caracteres Unicode en una secuencia de caracteres ASCII compatible, permitiendo su correcto funcionamiento en la web.

Para la implementación en Python se puede hacer uso de la biblioteca **idna**, que proporciona funciones para codificar y decodificar nombres de dominio Unicode a Punycode.
