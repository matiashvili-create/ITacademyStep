from functools import wraps

# გლობალური ცვლადები
SYSTEM_ACTIVE = True
GLOBAL_AUDIT_LOG = []


# დეკორატორი
def audit_system(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if SYSTEM_ACTIVE:
            GLOBAL_AUDIT_LOG.append(
                f"გამოძახებულია ფუნქცია: {func.__name__}"
            )

        return func(*args, **kwargs)

    return wrapper


# გარე ფუნქცია
def create_account_generator(initial_balance):

    balance = initial_balance
    transaction_id = 0

    # გენერატორი
    @audit_system
    def generator(amount):

        nonlocal balance, transaction_id

        balance += amount
        transaction_id += 1

        yield transaction_id, balance

    return generator


# პროგრამის გაშვება
account = create_account_generator(1000)

print(next(account(200)))
print(next(account(-100)))
print(next(account(500)))

print("აუდიტი: ")
print(GLOBAL_AUDIT_LOG)
   