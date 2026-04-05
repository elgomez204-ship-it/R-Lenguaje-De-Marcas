Introducción

Los documentos presentados son varios ejemplos de páginas HTML que integran JavaScript para añadir dinamismo e interactividad. A través de estos ejemplos se muestran operaciones básicas como la manipulación del DOM, el uso de variables, bucles y la modificación del contenido de una página web. En conjunto, representan una introducción práctica al uso de JavaScript dentro de HTML.

Aspectos técnicos

En estos ejemplos se utilizan conceptos fundamentales de JavaScript aplicados al entorno web:

Integración de JavaScript en HTML:
Se utiliza la etiqueta <script> para incluir código JavaScript dentro del documento HTML.
Variables y constantes:

Uso de const para almacenar datos:

const articulos = "Primer artículo","Segundo artículo","Tercer artículo";
Manipulación del DOM:
Selección de elementos con document.querySelector().

Ejemplo:

const contenedor = document.querySelector("main");
Bucles (for):

Se recorren arrays para generar contenido dinámico:

for(let i = 0; i < articulos.length; i++){
  contenedor.innerHTML += "<h3>"+articulos[i]+"</h3>";
}
Salida de información:
Uso de document.write() para mostrar contenido.
Uso de .textContent para obtener o insertar texto.
textContent inserta solo texto.
Uso de estilos con JavaScript:
Se modifican elementos con diferentes IDs #rojo, #verde, #azul para mostrar contenido dinámico.

¿Para qué sirve?

Estos ejemplos sirven para:

Aprender a conectar JavaScript con HTML.
Manipular elementos de una página web en tiempo real.
Generar contenido dinámico automáticamente.
Entender cómo funcionan los selectores del DOM.
Practicar estructuras básicas como bucles y arrays.
Dar los primeros pasos hacia el desarrollo web interactivo.

Son especialmente útiles para que las personas comprendan que están empezando con JavaScript en el navegador.

Conclusión

En conclusión, los ejemplos muestran de forma clara cómo JavaScript puede transformar una página HTML estática en una dinámica. Se aplican conceptos básicos como variables, bucles y manipulación del DOM, que son esenciales en el desarrollo web. Estos ejercicios constituyen una base sólida para avanzar hacia técnicas más avanzadas y buenas prácticas en JavaScript.