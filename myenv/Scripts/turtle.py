import turtle

def кох_кривая(черепаха, длина, уровень):
  """Рисует кривую Коха заданной длины и уровня."""
  if уровень == 0:
    черепаха.forward(длина)
  else:
    кох_кривая(черепаха, длина / 3, уровень - 1)
    черепаха.left(60)
    кох_кривая(черепаха, длина / 3, уровень - 1)
    черепаха.right(120)
    кох_кривая(черепаха, длина / 3, уровень - 1)
    черепаха.left(60)
    кох_кривая(черепаха, длина / 3, уровень - 1)

def снежинка_коха(черепаха, длина, уровень):
  """Рисует снежинку Коха заданной длины и уровня."""
  for _ in range(6):
    кох_кривая(черепаха, длина, уровень)
    черепаха.right(60)

# Настройка черепахи
черепаха = turtle.Turtle()
черепаха.speed(0)  # Самая быстрая скорость
черепаха.hideturtle()
черепаха.penup()
черепаха.goto(-200, 0)
черепаха.pendown()

# Рисование снежинки
снежинка_коха(черепаха, 400, 4)

# Ожидание, чтобы окно не закрывалось сразу
turtle.done()