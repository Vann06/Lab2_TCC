# Ejercicio 2 - Balanceador de Paréntesis

## 📋 Descripción
Este branch contiene la solución al **Ejercicio 2**: Implementación de un verificador de balance de paréntesis usando pilas.

## 🎥 Video de Presentación
**[Video de Presentación del Proyecto Completo](https://youtu.be/DyzjnCa10WI)**

---

## 📁 Archivos

### **balanceador.py** - Verificador de Balance de Paréntesis
- ✅ Verifica si los paréntesis están correctamente balanceados en expresiones
- 🔧 Utiliza un enfoque basado en pilas (stack)
- 📝 Soporta paréntesis `()`, corchetes `[]` y llaves `{}`
- 🎯 Detecta errores con precisión y ubicación exacta

### **expresiones.txt** - Expresiones de Prueba
- 📋 Contiene expresiones regulares para testing del balanceador
- 🧪 Casos complejos con múltiples niveles de anidación
- ❌ Incluye casos con errores para validar la detección

---

## 🚀 Instrucciones de Uso

```bash
python balanceador.py
```

### Ejemplo de salida:
```
Línea 1: a(a | b)*b + a?
  - Stack after adding '(': ['(']
  - Stack after removing ')': []
  - Expression is balanced: stack is empty
✓ RESULTADO: BALANCEADO
```

---

## �️ Algoritmo Implementado

### **Funcionamiento:**
1. **Inicializar pila vacía**
2. **Para cada carácter:**
   - Si es apertura `(`, `[`, `{` → PUSH a la pila
   - Si es cierre `)`, `]`, `}` → verificar coincidencia y POP
3. **Al final:** pila vacía = BALANCEADO

### **Complejidad:**
- ⚡ **Tiempo:** O(n) - lineal
- � **Espacio:** O(n) en el peor caso

---

## 🔗 Otros Ejercicios
- **Ejercicio 1:** Branch `ejercicio-1` (Solución PDF)
- **Ejercicio 3:** Branch `ejercicio-3` (Algoritmo Shunting Yard)
- **Proyecto Completo:** Branch `main` (Todos los ejercicios integrados)

---
**Desarrollado como parte del curso de Teoría de la Computación y Compiladores**
