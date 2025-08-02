# Lab 2 - Teoría de la Computación y Compiladores

Este proyecto implementa dos algoritmos fundamentales utilizados en el diseño de compiladores y teoría de lenguajes formales:

## 🎥 Video de Presentación

Mira la explicación completa y demostración de ambos algoritmos:
**[Video de Presentación del Proyecto](https://youtu.be/470yq2P1AhI)**

---

## 📁 Archivos del Proyecto

### 1. **balanceador.py** - Verificador de Balance de Paréntesis
   - ✅ Verifica si los paréntesis están correctamente balanceados en expresiones
   - 🔧 Utiliza un enfoque basado en pilas (stack)
   - 📝 Soporta paréntesis `()`, corchetes `[]` y llaves `{}`
   - 🎯 Detecta errores con precisión y ubicación exacta

### 2. **shunting_yard.py** - Algoritmo Shunting Yard
   - 🔄 Convierte expresiones regulares de notación infija a postfija
   - 🧠 Implementa el algoritmo Shunting Yard de Dijkstra
   - ⚖️ Maneja precedencia y asociatividad de operadores
   - 📊 Muestra el proceso de conversión paso a paso

### 3. **expresiones.txt** - Expresiones de Prueba
   - 📋 Contiene expresiones regulares de ejemplo para testing
   - 🧪 Utilizado por ambos programas para validación
   - 🔍 Incluye casos complejos y casos límite

---

## 🚀 Instrucciones de Uso

### Para verificar balance de paréntesis:
```bash
python balanceador.py
```

### Para convertir expresiones a notación postfija:
```bash
python shunting_yard.py
```

---

## 🛠️ Notas de Implementación

- 🎯 **Algoritmo Shunting Yard:** Requirió manejo cuidadoso de la precedencia de operadores
- 🔗 **Concatenación implícita:** Los operadores de concatenación se insertan automáticamente donde es necesario
- 🐛 **Manejo de errores:** Se agregó después de las pruebas iniciales que revelaron casos límite
- 📚 **Propósito educativo:** Ambos programas muestran ejecución paso a paso para fines de aprendizaje
- 💻 **Código limpio:** Implementación con variables en inglés y comentarios en español

---

## ⚙️ Operadores de Expresiones Regulares

| Operador | Precedencia | Asociatividad | Descripción |
|----------|-------------|---------------|-------------|
| `*`      | 3 (Alta)    | Derecha       | Estrella de Kleene (cero o más) |
| `+`      | 3 (Alta)    | Derecha       | Uno o más |
| `?`      | 3 (Alta)    | Derecha       | Cero o uno (opcional) |
| `.`      | 2 (Media)   | Izquierda     | Concatenación |
| `\|`     | 1 (Baja)    | Izquierda     | Alternación (OR) |

---

## 🧪 Casos de Prueba

El archivo `expresiones.txt` contiene varios casos de prueba incluyendo:

- ✅ **Alternaciones simples:** Expresiones básicas con operador `|`
- 🔄 **Paréntesis anidados:** Múltiples niveles de agrupación
- 🎯 **Expresiones regulares complejas:** Combinaciones de múltiples operadores
- 🐛 **Casos límite:** Expresiones que ayudaron a depurar la implementación
- ❌ **Casos con errores:** Para validar la detección de problemas

### Ejemplos de salida:

**Balanceador:**
```
Línea 1: a(a | b)*b + a?
✓ RESULTADO: BALANCEADO - Los paréntesis están correctamente emparejados
```

**Shunting Yard:**
```
EXPRESIÓN: a(a | b)*b + a?
Con concatenaciones: a.(a.|.b)*.b.+.a.?
✓ RESULTADO POSTFIJO: aab.|*.b+.a?.
```

---

## 🎓 Conceptos Teóricos Aplicados

- 📚 **Teoría de Autómatas:** Base teórica para expresiones regulares
- 🏗️ **Diseño de Compiladores:** Algoritmos fundamentales de parsing
- 🔧 **Estructuras de Datos:** Implementación eficiente de pilas
- 🧮 **Análisis Sintáctico:** Procesamiento de precedencia de operadores
- 🎯 **Complejidad Algorítmica:** Soluciones en tiempo lineal O(n)

---

## 👨‍💻 Información del Desarrollador

**Proyecto desarrollado como parte del curso de Teoría de la Computación y Compiladores**

- 🎯 Implementación desde cero de algoritmos clásicos
- 🧪 Testing exhaustivo con casos complejos
- 📝 Documentación detallada del proceso
- 🎥 Video explicativo completo disponible
