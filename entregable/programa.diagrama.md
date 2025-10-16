flowchart TD

%% --- INICIO Y CONFIGURACIÓN ---
A[Inicio] --> B[Definir constante DOC_FILENAME]
B --> C[Inicializar listaSecciones vacía]
C --> D[esPrimerTitulo ← Verdadero]
D --> E[nivelObjetivo ← 2]

%% --- BLOQUE DE LECTURA DE ARCHIVO ---
E --> F{Existe archivo DOC_FILENAME?}
F -->|No| G[Mostrar mensaje "Fichero no encontrado"]
G --> H[Fin del programa]
F -->|Sí| I[Leer archivo línea por línea]

I --> J{Línea es título y nivel = nivelObjetivo?}
J -->|Sí| K{esPrimerTitulo es Falso?}
K -->|Sí| L[Agregar sección anterior a listaSecciones]
K -->|No| M[esPrimerTitulo ← Falso]
L --> N[Guardar nuevo título y nivel]
M --> N
N --> O[Inicializar contenidoActual con salto de línea]
J -->|No y no esPrimerTitulo| P[Agregar línea al contenidoActual]
J -->|No y esPrimerTitulo| I
P --> I
I -->|Fin de archivo| Q[Agregar última sección a listaSecciones]

%% --- MENÚ PRINCIPAL ---
Q --> R[opcion ← -1]
R --> S[Mostrar menú con títulos numerados]
S --> T[Mostrar opción 0: Terminar programa]
T --> U[Leer opción del usuario]

%% --- SELECCIÓN DE OPCIÓN ---
U --> V{La opción es un número válido?}
V -->|No| W[Mostrar "Opción inválida"]
W --> S
V -->|Sí| X{opcion = 0?}
X -->|Sí| H
X -->|No| Y{opcion dentro del rango válido?}
Y -->|No| W
Y -->|Sí| Z[Mostrar título y contenido de la sección seleccionada]
Z --> S

%% --- FIN ---
H[Fin]
