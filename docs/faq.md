# Frequently asked questions (FAQ)

_Questions will arrive here. If you have a question not listed here, or the answer wasnt satisfactory, please contact us(Group 5, Marting and Bjørnar)_

Can I store a customer's email, address or name?
* No! You should never store anything other than the cid of a customer in your database(s). This is because information can change, but the cid will never change and always be the same customer. Read more here: [How everything works](/misc) and here: [How to store information tied to a customer](/usage#storing-information-tied-to-a-customer)

Why do I get this message in the response "The method is not allowed for the requested URL."?
* That is because you are using a request type that is not accepted for that route. For example if you try to send a GET request to Registration, which only accepts POST. So make sure you are using the correct type.