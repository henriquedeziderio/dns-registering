======================== DNS simple subset =============================
Developer: Henrique da Silva Deziderio


This program can register any domain from a Domain Name System (DNS), acknowledging the following records:
- A
- AAAA
- CNAME
- TXT

Running the Python program in a prompt, the user will see the following text:

-----------------------------------------------------------
DNS Subset
Developer: Henrique da Silva Deziderio

Choose your option:
1 - Register new DNS;
2 - Check DNS already registrated;
3 - Delete DNS;

Type 0 to exit.
-----------------------------------------------------------

The program gives to the user the option to type values among 0 to 3. If another number is typed, there will appear the following message:

-----------------------------------------------------------
Wrong option, choose a value among 0 to 3.
-----------------------------------------------------------

And the inicial menu appears again. If another kind of option is typed, like a string, for example, the program ends with an error and don't modify the source file.

On the 1st option, "Register new DNS", the user can type a simple domain name. This is not a case sensitive program. It means the typed domain will be automatically changed to upper case. For example, 'cname' will change to 'CNAME'. The new register will be put in the source file "registered_DNS". After registration is successful, a message of registration will appear and the inicial menu will follow the message.

The 2nd option gives to the user a list of the domains already registered.

Choosing the 3rd option, the user will can delete an already registered domain, except A, AAAA, CNAME and TXT.

CAUTION:
- The program doesn't run if the source file "registered_DNS" is not on the same directory of "DNS-register.py". It can be created a new empty file called "registered_DNS", no extension, but the file must be on the same directory. Doing that, all domain already registered except A, AAAA, CNAME and TXT will be deleted.
