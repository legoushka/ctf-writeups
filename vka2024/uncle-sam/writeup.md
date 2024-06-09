# Robbyry Of Uncle Sam #

Предоставленные [файлы](https://github.com/Red-Cadets/VKACTF-2024/tree/main/categories/pwn/pwn-1e-Robbery-of-Uncle-Sam/give):

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/4224eb5b-7f2f-43dd-94f3-021cc465bd92" alt="screen" width="200"/>

1. Проверим файл с помощью checksec, канарейка и PIE отключены.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/21de2105-ef6c-419a-b1e3-fff0fd59fcfc" alt="screen" width="400"/>


2. Проанализировав программу в гидре, видим переполнение буфера local_38.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/7d76f983-8a82-456f-9dd3-f298e257538a" alt="screen" width="500"/>


3. Рассчитаю количество байт необходимое для RIP Control, успешно перехватываю выполнение программы.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/5fc3b609-5a02-4963-b07a-140b70b8618c" alt="screen" width="450"/>


4. С помощью one_gadget (0xe3afe) нахожу в libc гаджет для получения шела.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/6dc48253-a012-49ef-b4fd-6b61d514bbcf" alt="screen" width="500"/>


5. Авторы задания также оставили функцию, которая поможет реализовать вышеописанный гаджет.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/d860690f-f91c-45ba-b808-519e0411f6d7" alt="screen" width="800"/>


6. С помощью ropper получаю pop rdi; ret; (0x4011a2) гаджет, в гидре нахожу адреса GOT (0x404000) и PLT (0x401030) для функции puts.

7. Пробую слить адрес puts в libc и прыгнунть на начало функции vuln(), успешно.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/d7c10498-f936-4e16-b4b0-5b0359a6e71e" alt="screen" width="450"/>
<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/16b07fea-6ab8-418d-a117-ebbe897fa6e5" alt="screen" width="400"/>

8. Находим оффсет puts относительно libc, теперь, мы можем высчитать базовый адрес libc по следующей формуле:

   base_libc = leaked_puts – 0x84420

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/4c115615-a76e-4476-a2e1-f6421a593c6b" alt="screen" width="500"/>

9. Дополним эксплойт, успешно получаем слитый базовый адрес libc.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/316c3b4d-fd1f-437d-aa00-58cb546a427e" alt="screen" width="1000"/>

10. Дополним эксплойт финальным этапом, которы воспользуется гаджетом для получения шелла.

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/54b900e6-c3f6-4f68-b501-63bded42378a" alt="screen" width="500"/>

11. Запускаем и успешно получаем шелл. Итоговая версия эксплойта может быть найдена тут: [solve.py](https://github.com/legoushka/ctf-writeups/blob/main/vka2024/uncle-sam/solve.py)

<img src="https://github.com/legoushka/ctf-writeups/assets/96149010/2ebea4e4-0dd9-48e5-9641-08860e276a4c" alt="screen" width="500"/>






