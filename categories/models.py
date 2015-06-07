from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=512)
    parent_name = models.CharField(max_length=512)
    budget = models.FloatField()
    amount = models.FloatField()
    date_of_budget = models.DateField()
    date_of_amount = models.DateField()
    type = models.CharField(max_length=16)
    level = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'catégories'


class CategoriesList(list):
    """Contient une liste d'objets category """

    def __init__(self, list_of_categories):
        super().__init__()
        self.list_of_categories = list_of_categories

    def __str__(self):
        s = "=" * 15 + " Class categorieslist " + "=" * 15 + "\n"
        for i in self:
            s += i.__str__() + "\n"

        s += "=" * 15 + " Class categorieslist " + "=" * 15 + "\n"
        return s

    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe , lève une exception KeyError sinon """
        # cat = Category
        cat = None
        for i in self:
            if i.name == cle:
                # print("Trouvé catégorie: {}".format(cle))
                cat = i
                # else:
                #    print("La catégorie {} n'existe pas.".format(cle))
                # cat = None
        if cat is None:
            raise KeyError("La catégorie {0} n'existe pas".format(cle))
        else:
            return cat

            # TODO: voir si cette fonction sert réellement (finalement) ?

    def index(self, value, start=None, stop=None):
        z = -1
        indice = 0
        for i in self:
            if i.name == value:
                indice = z
                print("Fonction 'Index' : Trouvé catégorie: {} à l'indice {}".format(value, indice))
            # else:
            # print("La catégorie {} n'existe pas.".format(value))
            z += 1
        if z < 0:
            raise KeyError("La catégorie {0} n'existe pas".format(value))
        else:
            return indice

    def parent_category(self, name):
        parent_categorie = self[name].parent_name
        return self[parent_categorie]

    def add_cat(self, category):
        pass

    def del_cat(self, category):
        pass

    def rename_cat(self, old_name, new_name):
        self[old_name].rename(new_name)

    def update_parent_budget(self, name, delta_budget):
        """ Cette fonction permet de mettre à jour le budget des catégories parentes lorsque que
        le budget d'une catégorie a changé

        :param name: Nom de la catégorie parente à changer
        :param delta_budget: on remplace la valeur du budget de la catégorie parente par le delta entre
        l'ancienne et la nouvelle valeur du budget de la sous-catégorie modifiée
        """
        self[name].budget += delta_budget
        if self[name].parent_name is not None:
            self.update_parent_budget(self[name].parent_name, delta_budget)

    def change_budget(self, name, value):
        """ Cette fonction remplace l'ancien budget de la catégorie par un nouveau budget. On appelle la fonction
        "update_parent_budget" pour mettre à jour les budgets des arborescence parentes

        :param name: Nom de la catégorie dont il faut modifier le budget
        :param value: Valeur du nouveau budget
        """
        old_budget = self[name].budget
        self[name].budget = value
        if self[name].parent_name is not None:  # TODO: vérifier si le test parent_name is not None est nécessaire
            # print("KKKKKKKKKKKKKKKKKKKKKKKKKKK",self[name].parent_name, "Delta montant: ", value - old_budget)
            self.update_parent_budget(self[name].parent_name, value - old_budget)

    def read_xml_file(self, list_of_elements, level):  # TODO: déverminer fonction read_xml_file
        level += 1
        # print('\n ++++  >>> ', level)
        # print("Montant = ", montant)
        for i in list_of_elements:
            j = i.getparent()
            # if list(i):
            #    read_xml_file(i, level)
            if level == 0:  # is not None:
                # print('Parent ("j") est égal à "None": ', j.attrib)
                cat = Category(i.attrib['text'], None)
                """ Pour le niveau zéro" on laisse le budget à zéro car le budget est calculé automatiquement\
                par l'appelle à la fonction update_parent_budget"""
                # cat.budget = float(i.attrib['Budget'])
                cat.amount = float(i.attrib['AmountAtDate'])
                cat.date_of_amount = "1970-01-01"
                cat.date_of_budget = i.attrib['Date']
                cat.type = i.attrib['type']
                cat.level = i.attrib['level']
                self.list_of_categories.append(cat)
            else:
                # print('Parent ("j") est différent de "None" ==>\
                #  Parent name = Existe -- Name = {1}','\n',i.attrib, '\n',j.attrib)
                cat = Category(i.attrib['text'], j.attrib['text'])

                if list(i):
                    """ Si la catégorie a une sous catégorie le budget est mis à zéro.\
                     il est ensuite calculé\
                    avec la fonction update_parent_budget"""
                    cat.budget = 0
                else:
                    cat.budget = float(i.attrib['Budget'])

                cat.amount_at_date = float(i.attrib['AmountAtDate'])
                cat.date_of_amount_at_date = "1970-01-01"
                cat.date_of_budget = i.attrib['Date']
                cat.type = i.attrib['type']
                cat.level = i.attrib['level']
                self.list_of_categories.append(cat)

                self.list_of_categories.update_parent_budget(cat.parent_name, cat.budget)  # - cat_parent.budget)

            if list(i):
                self.read_xml_file(i, level)

        return self.list_of_categories

    def write_xml_file(self, file_name):
        pass
