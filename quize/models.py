from django.db import models

class User(models.Model):
	user = models.CharField(max_length=50, verbose_name='код')
	def publish(self):
		self.save()

	def __str__(self):
		return self.user


class Category(models.Model):
	user  = models.ForeignKey(User)
	cat = models.CharField(max_length=200, choices = (
										    ('Спортивные', 'Спортивные'),
										    ('Интеллектуальные', 'Интеллектуальные'),
										    ('Творческие', 'Творческие'),
										), verbose_name='категория'
	)
	def __str__(self):
		return self.cat

class Contest(models.Model):
	cat  = models.ForeignKey(Category)
	name = models.CharField(max_length=200, verbose_name='название')
	day = models.CharField(max_length=200, choices = (
										    ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),
										    ('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),
										    ('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),
										    ('19', '19'),('20', '20'),('21', '21'),('22', '22'),('23', '23'),('24', '24'),
										    ('25', '25'),('26', '26'),('27', '27'),('28', '28'),('29', '29'),('30', '30'),('31', '31'),
										), verbose_name='день'
	)
	mont = models.CharField(max_length=200, choices = (
										    ('января', '1'),('февраля', '2'),('марта', '3'),('апреля', '4'),('мая', '5'),('июня', '6'),
										    ('июля', '7'),('августа', '8'),('сентября', '9'),('октября', '10'),('ноября', '11'),('декабря', '12'),
										), verbose_name='месяц'
	)
	year = models.CharField(max_length=200, choices = (
										    ('2000', '2000'),('2001', '2001'),('2002', '2002'),('2003', '2003'),('2004', '2004'),('2005', '2005'),
										    ('2006', '2006'),('2007', '2007'),('2008', '2008'),('2009', '2009'),('2010', '2010'),('2011', '2011'),
										    ('2012', '2012'),('2013', '2013'),('2014', '2014'),('2015', '2015'),('2016', '2016'),('2017', '2017'),
										), verbose_name='год'
	)
	result = models.CharField(max_length=20, choices = ( 
											('первое' , 'Первое'), ('второе' , 'Второе'), ('третье' , 'Третье'),('участие' , 'Участие'), 
										), verbose_name='место'
	)
	def __str__(self):
		return self.name

