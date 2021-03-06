---
layout: post
status: publish
published: true
date: '2018-04-24 09:15:06 +0200'
date_gmt: '2018-04-24 09:15:06 +0200'
lastmod: '2018-04-14 09:15:06 +0200'
title: El proyecto GDELT
categories:
- Documentación
tags:
- data engineering
- sentiment analysis
- cloud computing
- google
---
En el proceso para encontrar fuentes de datos, es habitual encontrar proyectos que tengan alguna característica excepcional en alguno de sus aspectos: el contenido, la tecnología o la metodología de análisis.

Esto tiene su lógica, ya que en muchos casos el foco del proyecto es en responder preguntas en un área concreta.

<!--more-->
Es por eso que me parece excepcional encontrar un proyecto como el de [GDELT][gdelt]{:target="_blank"}.

### La receta perfecta
Con unos ingredientes excepcionales:
* Alcance mundial, con traducción desde 65 idiomas.
* Uso de la tecnología de Google, tanto para la obtención del contenido como para su tratamiento. Esto incluye no sólo su traducción y análisis textual, sino también funcionalidades como *la detección de objetos en las fotografías*.
* Indexación y catalogación de las noticias mediante una serie de estándares (principalmente [CAMEO][cameo]{:target="_blank"}) que permiten integrar las noticias en múltiples contextos.
* Generación de indicadores y contenidos de forma automatizada.

¿Qué sucede si se recopila gran parte de la cobertura de los medios de todo el mundo y se intenta generar un mapa con las menciones de personas e instituciones, el tipo de reacciones que hay entre ellos, el sentimiento que se desprende de esos textos...?

Eso es el proyecto GDELT, que inicialmente surgió como un proyecto para anticiparse a los conflictos internacionales, y en especial a las crisis humanitarias.

### Uso de los datos y aplicaciones

El proyecto saca mucho jugo a los datos obtenidos, pero a su vez pone a disposición del público de manera gratuita la descarga de los enlaces a las noticias, las menciones que se han detectado en tales textos, el tono y otras [tecnologías][gdelt-computing]{:target="_blank"}, así como otros aspectos que se detallan [en el listado de datasets][gdelt-datasets]{:target="_blank"}.

En el camino que lleva al análisis de esos datos van generando cosas de utilidad como el [daily trend report][gdelt-daily-trend]{:target="_blank"} y el [world leaders index][gdelt-world-leaders]{:target="_blank"}.

Otra de las curiosidades son los gráficos incrustables sobre los indicadores analizados para la detección de conflictos. El siguiente es un gráfico del indicador de intensidad, descrito en [CAMEO][cameo]{:target="_blank"}, para la región de Estados Unidos. Es posible visualizar los indicadores para países y regiones administrativas más concretas.
<iframe
    border="0"
    src="https://api.gdeltproject.org/api/v1/dash_stabilitytimeline/dash_stabilitytimeline?LOC=US&VAR=conflict&OUTPUT=viz&NUMDAYS=4&TIMERES=15min&SMOOTH=3&AUTOCAP=2"
    width="100%"
    height="250">
</iframe>
### Fuentes de datos de libre disposición

El proyecto pone a disposición del público sin ningún cargo una serie de archivos para poder ser usados como se considere oportuno:
* Listado de los archivos CSV generados.
* Un archivo individual para cada franja de 15 minutos, incluyendo enlaces a las últimas noticias.
* Enlace a los lenguajes de catalogación/indexación/categorización utilizados.

Para más detalles, puedes ver los enlaces que hay al final de [este artículo en su blog sobre los datasets utilizados][gdelt-rawdata].

¡Buen provecho!


[gdelt]: https://www.gdeltproject.org/
[gdelt-datasets]: https://blog.gdeltproject.org/the-datasets-of-gdelt-as-of-february-2016/
[gdelt-computing]: https://www.gdeltproject.org/#computing
[gdelt-daily-trend]: https://blog.gdeltproject.org/gdelt-daily-trend-reports/
[gdelt-world-leaders]: https://blog.gdeltproject.org/new-gdelt-world-leaders-index/
[gdelt-rawdata]: https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/
[cameo]: https://en.wikipedia.org/wiki/Conflict_and_Mediation_Event_Observations
[jigsaw]: https://jigsaw.google.com/
[etl]: https://en.wikipedia.org/wiki/Extract,_transform,_load
