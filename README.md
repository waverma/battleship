# battleship - простая классическая 2D игра Морской бой
# Установка
git clone https://github.com/waverma/battleship
# Установка зависимостей
pip install -r requirements.txt
# Запуск
python3 \__main__.py либо py \__main__.py в директории battleship
# Правила
Размещаются: 1 корабль — ряд из 4 клеток («четырёхпалубные») 2 корабля — ряд из 3 клеток («трёхпалубные») 3 корабля — ряд из 2 клеток («двухпалубные») 4 корабля — 1 клетка («однопалубные»)
При размещении корабли не могут касаться друг друга сторонами и углами.
Попавший стреляет ещё раз.
# Управление
1) Начальная стадия: вид корабля для размещения выбирается автоматически. лкм поставить следующую часть корабля. Если при размещении корабль обозначен красным цветом, то ставить его в это место нельзя, если синим - можно. пкм - убрать корабль с поля. R - сгенерировать случайную карту. SPACE - повернуть корабль. Кнопка в бой - начать игру.
2) Стадия игры: лкм - выстрел. Зеленая клетка - промах. красная клетка - поврежденный корабль. синяя клетка - неповрежденный корабль. черная клетка - добитый корабль.
