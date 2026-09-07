# Análisis de la solución

## Objetivo

El objetivo de esta refactorización es mejorar la legibilidad y mantenibilidad
del código original de la kata Gilded Rose.

## Estrategia utilizada

Se ha aplicado una solución basada en el patrón Strategy.

Cada tipo de objeto dispone de una clase responsable de actualizar sus
atributos, evitando largas cadenas de condiciones.

## Mejoras obtenidas

- Menor complejidad ciclomática.
- Mejor separación de responsabilidades.
- Mayor facilidad para añadir nuevos tipos de objetos.
- Código más sencillo de probar.

## Conclusión

La solución mantiene el comportamiento esperado por la kata y mejora
la organización interna del código.
