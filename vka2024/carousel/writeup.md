# Santa-Maria Carousel writeup #

1. Программа принимает на вход строку и шифрует её. С заданием также шёл текстовый файл с криптограммой, которую нам необходимо расшифровать.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/5b0b56e9-4f22-45e4-9e97-23021be21f05" alt="screen" width="500"/>

2. Проанализируем .dll программы в [DIE](https://github.com/horsicq/Detect-It-Easy). Видим что используются C#, воспользуемся ILSpy для просмотра кода. 

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/77ac1d8d-68cc-4bf8-a857-109bc6f91b7e" alt="screen" width="400"/>

3. В первую очередь нас интересует фунцкия Cipher, всё остальные будут рассмотрены позже.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/da2aa253-3690-4d5b-9b00-c07931561a61" alt="screen" width="400"/>

4. Фунцкия шифрования имеет следующий вид. Как можно заметить исходный ключи констатный. Тажке, в конце имеются строки для вывода в дебаг информацию последнего ключа и использованных rotateKey (необходимых для преобразования исходного ключа).

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/ddcf8d3b-3b82-47d5-83f5-ff8de5ed6cfc" alt="screen" width="500"/>

5. Просмотрим дебаг информацию, убеждаемся, что ключи каждый раз используются одни и те же, вне зависимости от исходных данных. Мы сможем воспользоваться этими rotateKeys для преобразований ключа и составления списка ключей использованных по ходу шифрования исходного текста. Тажке мы сможем ориентироваться на последний ключ после преобразований выведенный в дебаг. Если последний из ключей которые мы сгенерируем совпадет с ключом из дебага, значит мы верно составили декриптор.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/e95184ce-8882-4160-b47c-32a96564333a" alt="screen" width="700"/>

6. Сгенерируем ключи следующим кодом. Не забудем добавить исходный ключ в лист.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/b3c46738-f7ce-4e5f-84b1-eedf59d34601" alt="screen" width="500"/>

7. Сравним сгенерированные ключи. 

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/c902fe47-2706-466e-a8c5-e2ed797ecffe" alt="screen" width="500"/>

8. Итоговый ключ совпадает, однако он нам не нужен, так как после преобразования ключа в последний раз, он не используется для шифрования сообщения. Поэтому закомментируем последний rotateKey.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/88bec929-a221-410f-8946-38ddf9940119" alt="screen" width="500"/>

9. Расшифровываем криптограмму и успешно получаем флаг.
<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/c2320f04-be09-4a4e-b24d-9a9ed7c9dd72" alt="screen" width="500"/>


