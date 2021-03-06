{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Выберите номер фильма из предложенных: Паразиты (1), 1917 (2), Соник в кино (3):  3\n",
      "Выберите дату: сегодня (1), завтра (2):  2\n",
      "Выберите доступное время сеанса (в формате 10:00 = 10):  18\n",
      "Укажите количество билетов:  23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 18:00 составит: 7762.5 рублей\n"
     ]
    }
   ],
   "source": [
    "a = int(input('Выберите номер фильма из предложенных: Паразиты (1), 1917 (2), Соник в кино (3): '))\n",
    "b = int(input('Выберите дату: сегодня (1), завтра (2): '))\n",
    "c = int(input('Выберите доступное время сеанса (в формате 10:00 = 10): '))\n",
    "d = int(input('Укажите количество билетов: '))\n",
    "\n",
    "        \n",
    "# для фильма \"Паразиты\"\n",
    "        \n",
    "if a == 1 and b == 1 and c == 12 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 12:00 составит:', 250*d, \"рублей\")    \n",
    "elif a == 1 and b == 1 and c == 12 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 12:00 составит:', 250*d*0.8, \"рублей\")\n",
    "elif a == 1 and b == 2 and c == 12 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 12:00 составит:', 250*d*0.95, \"рублей\")    \n",
    "elif a == 1 and b == 2 and c == 12 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 12:00 составит:', 250*d*0.75, \"рублей\")\n",
    "        \n",
    "elif a == 1 and b == 1 and c == 16 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 16:00 составит:', 350*d, \"рублей\") \n",
    "elif a == 1 and b == 1 and c == 16 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 16:00 составит:', 350*d*0.8, \"рублей\")\n",
    "elif a == 1 and b == 2 and c == 16 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 16:00 составит:', 350*d*0.95, \"рублей\")    \n",
    "elif a == 1 and b == 2 and c == 16 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 16:00 составит:', 350*d*0.75, \"рублей\")      \n",
    "        \n",
    "elif a == 1 and b == 1 and c == 20 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 20:00 составит:', 450*d, \"рублей\")\n",
    "elif a == 1 and b == 1 and c == 20 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс сегодня в 20:00 составит:', 450*d*0.8, \"рублей\")\n",
    "elif a == 1 and b == 2 and c == 20 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 20:00 составит:', 450*d*0.95, \"рублей\")    \n",
    "elif a == 1 and b == 2 and c == 20 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Паразиты\", сеанс завтра в 20:00 составит:', 450*d*0.75, \"рублей\")\n",
    "        \n",
    "# для фильма \"1917\"\n",
    "        \n",
    "elif a == 2 and b == 1 and c == 10 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 10:00 составит:', 250*d, \"рублей\")    \n",
    "elif a == 2 and b == 1 and c == 10 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 10:00 составит:', 250*d*0.8, \"рублей\")\n",
    "elif a == 2 and b == 2 and c == 10 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 10:00 составит:', 250*d*0.95, \"рублей\")    \n",
    "elif a == 2 and b == 2 and c == 10 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 10:00 составит:', 250*d*0.75, \"рублей\")\n",
    "        \n",
    "elif a == 2 and b == 1 and c == 13 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 13:00 составит:', 350*d, \"рублей\")\n",
    "elif a == 2 and b == 1 and c == 13 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 13:00 составит:', 350*d*0.8, \"рублей\")\n",
    "elif a == 2 and b == 2 and c == 13 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 13:00 составит:', 350*d*0.95, \"рублей\")    \n",
    "elif a == 2 and b == 2 and c == 13 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 13:00 составит:', 350*d*0.75, \"рублей\")\n",
    "        \n",
    "elif a == 2 and b == 1 and c == 16 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 16:00 составит:', 350*d, \"рублей\") \n",
    "elif a == 2 and b == 1 and c == 16 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс сегодня в 16:00 составит:', 350*d*0.8, \"рублей\")\n",
    "elif a == 2 and b == 2 and c == 16 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 16:00 составит:', 350*d*0.95, \"рублей\")    \n",
    "elif a == 2 and b == 2 and c == 16 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"1917\", сеанс завтра в 16:00 составит:', 350*d*0.75, \"рублей\")      \n",
    "        \n",
    "# для фильма \"Соник в кино\"\n",
    "        \n",
    "elif a == 3 and b == 1 and c == 10 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 10:00 составит:', 350*d, \"рублей\")    \n",
    "elif a == 3 and b == 1 and c == 10 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 10:00 составит:', 350*d*0.8, \"рублей\")\n",
    "elif a == 3 and b == 2 and c == 10 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 10:00 составит:', 350*d*0.95, \"рублей\")    \n",
    "elif a == 3 and b == 2 and c == 10 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 10:00 составит:', 350*d*0.75, \"рублей\")\n",
    "        \n",
    "elif a == 3 and b == 1 and c == 14 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 14:00 составит:', 450*d, \"рублей\")\n",
    "elif a == 3 and b == 1 and c == 14 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 14:00 составит:', 450*d*0.8, \"рублей\")\n",
    "elif a == 3 and b == 2 and c == 14 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 14:00 составит:', 450*d*0.95, \"рублей\")    \n",
    "elif a == 3 and b == 2 and c == 14 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 14:00 составит:', 450*d*0.75, \"рублей\")\n",
    "        \n",
    "elif a == 3 and b == 1 and c == 18 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 18:00 составит:', 450*d, \"рублей\") \n",
    "elif a == 3 and b == 1 and c == 18 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс сегодня в 18:00 составит:', 450*d*0.8, \"рублей\")\n",
    "elif a == 3 and b == 2 and c == 18 and d < 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 18:00 составит:', 450*d*0.95, \"рублей\")    \n",
    "elif a == 3 and b == 2 and c == 18 and d >= 20:\n",
    "    print('Стоимость билетов на фильм \"Соник в кино\", сеанс завтра в 18:00 составит:', 450*d*0.75, \"рублей\") \n",
    "        \n",
    "else: \n",
    "    print('Сеанс не найден!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
