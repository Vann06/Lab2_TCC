# Ejercicio 3 - Algoritmo Shunting Yard

## 📋 Descripción
Este branch contiene la solución al **Ejercicio 3**: Implementación del algoritmo Shunting Yard para conversión de expresiones regulares de notación infija a postfija.

## 🎥 Video de Presentación
**[Video de Presentación del Proyecto Completo](https://youtu.be/DyzjnCa10WI)**

---

## 📁 Archivos

### **shunting_yard.py** - Algoritmo Shunting Yard
- 🔄 Convierte expresiones regulares de notación infija a postfija
- 🧠 Implementa el algoritmo Shunting Yard de Dijkstra (1961)
- ⚖️ Maneja precedencia y asociatividad de operadores automáticamente
- 📊 Muestra el proceso de conversión paso a paso
- 🔗 Inserta concatenaciones implícitas donde es necesario

### **expresiones.txt** - Expresiones de Prueba
- 📋 Contiene expresiones regulares complejas para testing
- 🧪 Casos con múltiples operadores y niveles de precedencia
- 🎯 Expresiones que validan el manejo correcto de asociatividad

---

## 🚀 Instrucciones de Uso

```bash
python shunting_yard.py
```

### Ejemplo de salida:
```
==================================================
EXPRESIÓN 1: a(a | b)*b + a?
==================================================
Con concatenaciones: a.(a.|.b)*.b.+.a.?
Proceso paso a paso:
   1. Operando 'a' → salida: ['a']
   2. Operador '.' → pila: ['.']
   ...
✓ RESULTADO FINAL: aab.|*.b+.a?.
```

---

## ⚙️ Operadores Soportados

| Operador | Precedencia | Asociatividad | Descripción |
|----------|-------------|---------------|-------------|
| `*`      | 3 (Alta)    | Derecha       | Estrella de Kleene (cero o más) |
| `+`      | 3 (Alta)    | Derecha       | Uno o más |
| `?`      | 3 (Alta)    | Derecha       | Cero o uno (opcional) |
| `.`      | 2 (Media)   | Izquierda     | Concatenación |
| `\|`     | 1 (Baja)    | Izquierda     | Alternación (OR) |

---

## 🛠️ Algoritmo Implementado

### **Pasos del Shunting Yard:**
1. **Insertar concatenaciones explícitas** donde sea necesario
2. **Procesar cada token:**
   - Operandos → directamente a la salida
   - `(` → push a la pila
   - `)` → vaciar hasta encontrar `(`
   - Operadores → aplicar reglas de precedencia
3. **Vaciar pila restante** a la salida final

### **Complejidad:**
- ⚡ **Tiempo:** O(n) - procesamiento lineal
- 💾 **Espacio:** O(n) para pila y salida

---

## � Casos de Prueba Destacados

- ✅ **Expresión 1:** `a(a | b)*b + a?` → `aab.|*.b+.a?.`
- ✅ **Expresión 6:** Anidación compleja con 6 niveles de paréntesis
- 🔧 **Manejo de concatenación:** Inserción automática de puntos
- 🎪 **Precedencia correcta:** Operadores de alta precedencia primero

---

## 🔗 Otros Ejercicios
- **Ejercicio 1:** Branch `ejercicio-1` (Solución PDF)
- **Ejercicio 2:** Branch `ejercicio-2` (Balanceador de Paréntesis)
- **Proyecto Completo:** Branch `main` (Todos los ejercicios integrados)

---
**Desarrollado como parte del curso de Teoría de la Computación y Compiladores**
