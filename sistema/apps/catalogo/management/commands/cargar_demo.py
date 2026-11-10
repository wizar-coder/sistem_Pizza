from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.catalogo.models import Categoria, Producto

CATEGORIAS = [
    ("Pizzas", "Pizzas artesanales con masa fresca y horno de piedra."),
    ("Promos y combos", "Combinaciones para una o varias personas."),
    ("Entradas", "Acompañamientos y entradas."),
    ("Bebidas", "Bebidas frías y refrescos."),
    ("Postres", "Postres de la casa."),
]

# (categoría, nombre, descripción, precio en soles)
PRODUCTOS = [
    ("Pizzas", "Pizza Margarita (personal)", "Salsa de tomate, mozzarella y albahaca fresca.", "18.00"),
    ("Pizzas", "Pizza Margarita (familiar)", "Salsa de tomate, mozzarella y albahaca fresca. 8 porciones.", "38.00"),
    ("Pizzas", "Pizza Pepperoni (personal)", "Salsa de tomate, mozzarella y pepperoni.", "22.00"),
    ("Pizzas", "Pizza Pepperoni (familiar)", "Salsa de tomate, mozzarella y pepperoni. 8 porciones.", "45.00"),
    ("Pizzas", "Pizza Hawaiana (personal)", "Salsa de tomate, mozzarella, jamón y piña.", "22.00"),
    ("Pizzas", "Pizza Hawaiana (familiar)", "Salsa de tomate, mozzarella, jamón y piña. 8 porciones.", "45.00"),
    ("Pizzas", "Pizza Suprema (personal)", "Mozzarella, jamón, pepperoni, champiñones, aceitunas y pimiento.", "26.00"),
    ("Pizzas", "Pizza Suprema (familiar)", "Mozzarella, jamón, pepperoni, champiñones, aceitunas y pimiento. 8 porciones.", "52.00"),
    ("Pizzas", "Pizza Cuatro Quesos (familiar)", "Mozzarella, parmesano, provolone y queso azul. 8 porciones.", "50.00"),
    ("Pizzas", "Pizza Vegetariana (personal)", "Mozzarella, champiñones, pimiento, cebolla y aceitunas.", "24.00"),
    ("Pizzas", "Pizza Vegetariana (familiar)", "Mozzarella, champiñones, pimiento, cebolla y aceitunas. 8 porciones.", "48.00"),
    ("Promos y combos", "Combo familiar", "2 pizzas familiares, papas grandes y gaseosa de 1.5 litros.", "99.00"),
    ("Promos y combos", "Combo pareja", "1 pizza familiar, 6 alitas BBQ y 2 gaseosas personales.", "69.00"),
    ("Promos y combos", "Combo personal", "1 pizza personal, porción de papas y gaseosa personal.", "27.00"),
    ("Entradas", "Alitas BBQ (8 uds)", "Alitas de pollo glaseadas con salsa BBQ.", "26.00"),
    ("Entradas", "Alitas acevichadas (8 uds)", "Alitas de pollo con salsa acevichada de la casa.", "26.00"),
    ("Entradas", "Papas fritas", "Porción de papas fritas crocantes.", "9.00"),
    ("Entradas", "Papas con queso", "Papas fritas con queso fundido y tocino.", "14.00"),
    ("Entradas", "Pan de ajo", "Pan de ajo con mantequilla y perejil.", "8.00"),
    ("Entradas", "Ensalada fresca", "Lechuga, tomate, zanahoria y limón.", "8.00"),
    ("Bebidas", "Chicha morada (jarra)", "Jarra de chicha morada de la casa.", "12.00"),
    ("Bebidas", "Chicha morada (vaso)", "Vaso de chicha morada de la casa.", "4.00"),
    ("Bebidas", "Limonada (jarra)", "Jarra de limonada fresca de la casa.", "12.00"),
    ("Bebidas", "Inca Kola 500 ml", "Gaseosa Inca Kola personal.", "5.00"),
    ("Bebidas", "Coca-Cola 500 ml", "Gaseosa Coca-Cola personal.", "5.00"),
    ("Bebidas", "Agua mineral", "Botella de agua mineral sin gas.", "3.00"),
    ("Postres", "Flan casero", "Flan de la casa con caramelo.", "7.00"),
    ("Postres", "Mazamorra morada", "Mazamorra morada tradicional.", "6.00"),
    ("Postres", "Brownie con helado", "Brownie de chocolate con helado de vainilla.", "12.00"),
]


class Command(BaseCommand):
    help = "Carga categorías y productos de ejemplo para probar el sistema (idempotente)."

    def handle(self, *args, **options):
        categorias_nuevas = 0
        for orden, (nombre, descripcion) in enumerate(CATEGORIAS, start=1):
            _, creada = Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={"descripcion": descripcion, "orden": orden, "activo": True},
            )
            categorias_nuevas += int(creada)

        productos_nuevos = 0
        for categoria_nombre, nombre, descripcion, precio in PRODUCTOS:
            categoria = Categoria.objects.get(nombre=categoria_nombre)
            _, creado = Producto.objects.get_or_create(
                categoria=categoria,
                nombre=nombre,
                defaults={
                    "descripcion": descripcion,
                    "precio": Decimal(precio),
                    "activo": True,
                },
            )
            productos_nuevos += int(creado)

        self.stdout.write(self.style.SUCCESS(
            f"Categorías nuevas: {categorias_nuevas}. Productos nuevos: {productos_nuevos}."
        ))
