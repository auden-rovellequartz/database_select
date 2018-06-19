# -*- coding: utf-8 -*-

def home():
	list_of_recipes = TABLE()
	recipes_rows = db(db.recipes.id > 0).select()
	for x in recipes_rows:
		list_of_recipes.append(
			TR(x.recipe)
			)
	select_recipe = A(
		"select your favorite recipe",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "select",
			)
		)
	view_selections = A(
		"view recipe selections",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "selections",
			)
		)
	form = FORM(
		DIV(
			LABEL("Register a Recipe: "),
			INPUT(
				_type = "text",
				_name = "recipe",
				),
			),
		INPUT(
			_type = "submit",
			_value = "Register",
			)
		)
	if (form.process().accepted):
		db.recipes.insert(
			recipe = form.vars.recipe,
			)
		db.commit()
		redirect(
			URL(
				a = "database_select",
				c = "c01",
				f = "home",
				)
			)
	return dict(
		form = form,
		list_of_recipes = list_of_recipes,
		select_recipe = select_recipe,
		view_selections = view_selections,
		)
def select():
	list_of_recipes = [""]
	recipes_rows = db(db.recipes.id > 0).select()
	for x in recipes_rows:
		list_of_recipes.append(x.recipe)
	home = A(
		"Register a Recipe",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "home",
			)
		)
	view_selections = A(
		"view recipe selections",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "selections",
			)
		)
	form = FORM(
		DIV(
			LABEL("Your Name: "),
			INPUT(
				_type = "text",
				_name = "name",
				),
			),
		DIV(
			LABEL("Select Your Favorite Recipe: "),
			SELECT(
				_type = "select",
				_name = "favorite",
				*[OPTION(x) for x in list_of_recipes]
				),
			),
		INPUT(
			_type = "submit",
			_value = "Submit Favorite",
			)
		)
	if (form.process().accepted):
		db.favorites.insert(
			person = form.vars.name,
			recipe = form.vars.favorite,
			)
		db.commit()
		redirect(
			URL(
				a = "database_select",
				c = "c01",
				f = "home",
				)
			)
	return dict(
		form = form,
		home = home,
		view_selections = view_selections,
		)
def selections():
	home = A(
		"Register a Recipe",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "home",
			)
		)
	select_recipe = A(
		"select your favorite recipe",
		_href = URL(
			a = "database_select",
			c = "c01",
			f = "select",
			)
		)
	selections = TABLE()
	favorites_rows = db(db.favorites.id > 0).select()
	for x in favorites_rows:
		selections.append(
			TR(
				TD(x.person),
				TD(x.recipe),
				)
			)
	return dict(
		selections = selections,
		home = home,
		select_recipe = select_recipe,
		)
