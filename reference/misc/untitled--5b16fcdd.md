---
doc_id: "mta-wiki:9629"
title: "Аккаунт"
source_title: "Аккаунт"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82"
revision_id: 69939
language: "en"
categories: ["Понятия_скриптинга"]
generated_at: "2026-07-26T16:17:08.599627+00:00"
---

# Аккаунт

Класс аккаунт представляет собой набор данных о пользователе, или, как это принято упоминать, об [игроке](https://wiki.multitheftauto.com/wiki/RU/Element/Player). Вы можете получить аккаунт, связанный с любым клиентом, используя функцию [getPlayerAccount](https://wiki.multitheftauto.com/wiki/RU/getPlayerAccount).

Аккаунты уникальны для каждого клиента и могут использоваться для хранения информации, которая постоянно сохраняется при пользовательских сеансах. Клиентам, которые присоединяются без аккаунта, предоставляется временный аккаунт *guest* (гость). Этот аккаунт может хранить информацию, как и любой другой аккаунт, но разница лишь в том, что он не сохраняется после сеанса.

Когда пользователь входит в систему или выходит из неё, аккаунт, назначенный им, изменится. Таким образом, Вы не должны предполагать, что аккаунт, прикрепленный к клиенту, остаётся постоянным во время сеанса.

PHP-код для проверки хэшей паролей из базы данных сервера MTA находится [здесь](mta://reference/misc/account-php.md).

## Связанные функции

### Сервер

#### Серверные функции

- [addAccount](https://wiki.multitheftauto.com/wiki/RU/addAccount) - *регистрирует аккаунт*

- [copyAccountData](https://wiki.multitheftauto.com/wiki/RU/copyAccountData) - *копирует данные аккаунта в другой*

- [getAccount](https://wiki.multitheftauto.com/wiki/RU/getAccount) - *получает аккаунт указанного пользователя*

- [getAccountByID](https://wiki.multitheftauto.com/wiki/RU/getAccountByID) - *получает аккаунт с указанным ID*

- [getAccountData](https://wiki.multitheftauto.com/wiki/RU/getAccountData) - *получает указанные данные аккаунта*

- [getAccountID](https://wiki.multitheftauto.com/wiki/RU/getAccountID) - *получает ID указанного аккаунта*

- [getAccountIP](https://wiki.multitheftauto.com/wiki/RU/getAccountIP) - *получает IP указанного аккаунта*

- [getAccountName](https://wiki.multitheftauto.com/wiki/RU/getAccountName) - *получает имя аккаунта*

- [getAccountPlayer](https://wiki.multitheftauto.com/wiki/RU/getAccountPlayer) - *получает активного пользователя аккаунта*

- [getAccountSerial](https://wiki.multitheftauto.com/wiki/RU/getAccountSerial) - *получает серийный номер аккаунта*

- [getAccounts](https://wiki.multitheftauto.com/wiki/RU/getAccounts) - *получает все зарегистрированные аккаунты*

- [getAccountsByData](https://wiki.multitheftauto.com/wiki/RU/getAccountsByData) - *получает аккаунты с указанными сохранёнными данными*

- [getAccountsByIP](https://wiki.multitheftauto.com/wiki/RU/getAccountsByIP) - *получает аккаунт с указанным IP*

- [getAccountsBySerial](https://wiki.multitheftauto.com/wiki/RU/getAccountsBySerial) - *получает все аккаунты с указанным серийным номером*

- [getAllAccountData](https://wiki.multitheftauto.com/wiki/RU/getAllAccountData) - *получает все данные аккаунта*

- [getPlayerAccount](https://wiki.multitheftauto.com/wiki/RU/getPlayerAccount) - *получает аккаунт указанного игрока*

- [isGuestAccount](https://wiki.multitheftauto.com/wiki/RU/isGuestAccount) - *проверяет, является ли аккаунт гостевым*

- [logIn](https://wiki.multitheftauto.com/wiki/RU/logIn) - *авторизует игрока под указанный аккаунт*

- [logOut](https://wiki.multitheftauto.com/wiki/RU/logOut) - *выходит из аккаунта указанного игрока*

- [removeAccount](https://wiki.multitheftauto.com/wiki/RU/removeAccount) - *удаляет аккаунт*

- [setAccountData](https://wiki.multitheftauto.com/wiki/RU/setAccountData) - *сохраняет данные в аккаунте*

- [setAccountName](https://wiki.multitheftauto.com/wiki/RU/setAccountName) - *устанавливает имя аккаунту*

- [setAccountPassword](https://wiki.multitheftauto.com/wiki/RU/setAccountPassword) - *устанавливает пароль аккаунта*
