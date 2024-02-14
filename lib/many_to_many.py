class Author:
    
    all=[]

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        pass

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

    pass


class Book:
    
    all=[]

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

        pass

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

    pass


class Contract:

    all=[]

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        if isinstance(date, str):          
            self.date = date
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception
        Contract.all.append(self)
        pass

    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]
    pass