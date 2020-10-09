{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Для того, чтобы перевести Цельсий в Фаренгейт, нужно нажать 1\n",
      " Для того, чтобы перевести Фаренгейт в Цельсий, нужно нажать 2\n",
      "2\n",
      "Сколько градусов по Фаренгейту? :\n",
      "56\n",
      "56 градусов по Фаренгейту составляют -18.9 градусов по Цельсию\n"
     ]
    }
   ],
   "source": [
    "import string \n",
    "\n",
    "vvod = input(' Для того, чтобы перевести Цельсий в Фаренгейт, нужно нажать 1\\n Для того, чтобы перевести Фаренгейт в Цельсий, нужно нажать 2\\n')\n",
    "if not vvod.isdigit():   #проверяем, если не только цифры...ошибка\n",
    "    print('нужно ввести число')\n",
    "    exit(1)\n",
    "vv = int(vvod)  #если все же цифры, то переводим в целое число\n",
    "if not(1 <= vv <= 2): #если не 1 и не 2...ошибка\n",
    "    print('нужно ввести 1 или 2')\n",
    "    exit(1)\n",
    "\n",
    "    \n",
    "otr = '\"-\"\".\"0123456789'\n",
    "    \n",
    "if vv == 1:\n",
    "    temp = input('Сколько градусов по Цельсию? Нужно ввести число :\\n')\n",
    "    \n",
    "    if temp[:] not in otr:\n",
    "        print('не число')\n",
    "        exit(1)\n",
    "        n=float(temp)\n",
    "        #(0 °C × 9/5) + 32 = 32 °F через round округляем до 1 числа после запятой\n",
    "    print(temp, 'градусов по Цельсию вы ввели.', round(((n * (9/5) +32)), 1),'градусов по Фаренгейту вы получили')\n",
    "    \n",
    "elif vv == 2:\n",
    "    temp = input('Сколько градусов по Фаренгейту? Нужно ввести число :\\n')\n",
    "    \n",
    "    if temp[:] not in otr:\n",
    "        print('не число')\n",
    "        exit(1)    \n",
    "        n=float(temp)\n",
    "        #(273 °F − 32) × 5/9 = 133,889 °C\n",
    "    print(temp, 'градусов по Фаренгейту вы ввели.', round(((n - 32) * (5/9)), 1),'градусов по Цельсию вы получили')"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
