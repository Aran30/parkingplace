####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Enumerations
Genre: Enumeration = Enumeration(
    name="Genre",
    literals={
            EnumerationLiteral(name="Poetry"),
			EnumerationLiteral(name="Thriller"),
			EnumerationLiteral(name="History"),
			EnumerationLiteral(name="Technology"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="Philosophy"),
			EnumerationLiteral(name="Cookbooks"),
			EnumerationLiteral(name="Fantasy")
    }
)

# Classes
Book = Class(name="Book")
Library = Class(name="Library")
Author = Class(name="Author")
Publisher = Class(name="Publisher")

# Book class attributes and methods
Book_title: Property = Property(name="title", type=StringType)
Book_pages: Property = Property(name="pages", type=IntegerType)
Book_stock: Property = Property(name="stock", type=IntegerType)
Book_price: Property = Property(name="price", type=FloatType)
Book_release: Property = Property(name="release", type=DateType)
Book_genre: Property = Property(name="genre", type=Genre)
Book_m_decrease_stock: Method = Method(name="decrease_stock", parameters={Parameter(name='qty', type=IntegerType)}, implementation_type=MethodImplementationType.CODE)
Book_m_decrease_stock.code = """def decrease_stock(self, qty: int):
    \"\"\"
    Decrease the available stock by the given quantity.

    :param qty: Number of items to remove from stock
    :raises ValueError: If qty is negative or exceeds available stock
    \"\"\"
    if qty <= 0:
        raise ValueError("Quantity must be a positive integer")

    if qty > self.stock:
        raise ValueError(
            f"Cannot decrease stock by {qty}. Only {self.stock} items available."
        )

    self.stock -= qty

"""
Book.attributes={Book_genre, Book_pages, Book_price, Book_release, Book_stock, Book_title}
Book.methods={Book_m_decrease_stock}

# Library class attributes and methods
Library_name: Property = Property(name="name", type=StringType)
Library_web_page: Property = Property(name="web_page", type=StringType)
Library_address: Property = Property(name="address", type=StringType)
Library_telephone: Property = Property(name="telephone", type=StringType)
Library_m_cheapest_book_by: Method = Method(name="cheapest_book_by", parameters={Parameter(name='author', type=Author)}, type=StringType, implementation_type=MethodImplementationType.BAL)
Library_m_cheapest_book_by.code = """def cheapest_book_by(author:Author) -> str {
    cheapest:Book = null;
	price = 1000000000.0;
	for(book in this.books){
        if(book.authors.contains(author)
			&& book.price <= price){
            cheapest = book;
			price = book.price;
		}
    }
	return cheapest.title;
}"""
Library.attributes={Library_address, Library_name, Library_telephone, Library_web_page}
Library.methods={Library_m_cheapest_book_by}

# Author class attributes and methods
Author_birth: Property = Property(name="birth", type=DateType)
Author_name: Property = Property(name="name", type=StringType)
Author.attributes={Author_birth, Author_name}

# Publisher class attributes and methods
Publisher_name: Property = Property(name="name", type=StringType)
Publisher_address: Property = Property(name="address", type=StringType)
Publisher_telephone: Property = Property(name="telephone", type=StringType)
Publisher.attributes={Publisher_address, Publisher_name, Publisher_telephone}

# Relationships
books: BinaryAssociation = BinaryAssociation(
    name="books",
    ends={
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
books_1: BinaryAssociation = BinaryAssociation(
    name="books_1",
    ends={
        Property(name="authors", type=Author, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
Publisher_Book: BinaryAssociation = BinaryAssociation(
    name="Publisher_Book",
    ends={
        Property(name="publisher", type=Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
constraint_Book_0_1: Constraint = Constraint(
    name="constraint_Book_0_1",
    context=Book,
    expression="context Book inv inv1: self.pages> 10",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Book, Library, Author, Publisher, Genre},
    associations={books, books_1, Publisher_Book},
    constraints={constraint_Book_0_1},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Book", view_elements=set(), is_main_page=True, route_path="/book", screen_size="Medium")
wrapper.component_id = "page-book-0"
ivqvh = Text(
    name="ivqvh",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ivqvh",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ivqvh"}
)
i4h9i = Link(
    name="i4h9i",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4h9i",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i4h9i"}
)
i8bxt = Link(
    name="i8bxt",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8bxt",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i8bxt"}
)
iwe4v = Link(
    name="iwe4v",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwe4v",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "iwe4v"}
)
i9zlf = Link(
    name="i9zlf",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9zlf",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "i9zlf"}
)
it17f = ViewContainer(
    name="it17f",
    description=" component",
    view_elements={i4h9i, i8bxt, iwe4v, i9zlf},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="it17f",
    display_order=1,
    custom_attributes={"id": "it17f"}
)
it17f_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
it17f.layout = it17f_layout
icx3g = Text(
    name="icx3g",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="icx3g",
    display_order=2,
    custom_attributes={"id": "icx3g"}
)
i6ido = ViewContainer(
    name="i6ido",
    description="nav container",
    view_elements={ivqvh, it17f, icx3g},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i6ido",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i6ido"}
)
i6ido_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i6ido.layout = i6ido_layout
i2s5v = Text(
    name="i2s5v",
    content="Book",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i2s5v",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i2s5v"}
)
irbyp = Text(
    name="irbyp",
    content="Manage Book data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="irbyp",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "irbyp"}
)
table_book_0_col_0 = FieldColumn(label="Title", field=Book_title)
table_book_0_col_1 = FieldColumn(label="Pages", field=Book_pages)
table_book_0_col_2 = FieldColumn(label="Stock", field=Book_stock)
table_book_0_col_3 = FieldColumn(label="Price", field=Book_price)
table_book_0_col_4 = FieldColumn(label="Release", field=Book_release)
table_book_0_col_5 = FieldColumn(label="Genre", field=Book_genre)
table_book_0_col_6_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "library")
table_book_0_col_6 = LookupColumn(label="Library", path=table_book_0_col_6_path, field=Library_name)
table_book_0_col_7_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "authors")
table_book_0_col_7 = LookupColumn(label="Authors", path=table_book_0_col_7_path, field=Author_name)
table_book_0 = Table(
    name="table_book_0",
    title="Book List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_book_0_col_0, table_book_0_col_1, table_book_0_col_2, table_book_0_col_3, table_book_0_col_4, table_book_0_col_5, table_book_0_col_6, table_book_0_col_7],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-book-0",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Book List", "data-source": "class_oho5ergc3_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'title', 'label': 'Title', 'columnType': 'field', '_expanded': False}, {'field': 'pages', 'label': 'Pages', 'columnType': 'field', '_expanded': False}, {'field': 'stock', 'label': 'Stock', 'columnType': 'field', '_expanded': False}, {'field': 'price', 'label': 'Price', 'columnType': 'field', '_expanded': False}, {'field': 'release', 'label': 'Release', 'columnType': 'field', '_expanded': False}, {'field': 'genre', 'label': 'Genre', 'columnType': 'field', '_expanded': False}, {'field': 'library', 'label': 'Library', 'columnType': 'lookup', 'lookupEntity': 'class_06blhjj3h_mjikkmod', 'lookupField': 'name', '_expanded': False}, {'field': 'authors', 'label': 'Authors', 'columnType': 'lookup', 'lookupEntity': 'class_d3f0di6lb_mjikkmoe', 'lookupField': 'name', '_expanded': False}, {'field': 'Publisher', 'label': 'Publisher', 'columnType': 'lookup', 'lookupEntity': 'class_o32xm5mdp_moil1glk_pd3', 'lookupField': 'name', '_expanded': False}], "id": "table-book-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_book_0_binding_domain = None
if domain_model_ref is not None:
    table_book_0_binding_domain = domain_model_ref.get_class_by_name("Book")
if table_book_0_binding_domain:
    table_book_0_binding = DataBinding(domain_concept=table_book_0_binding_domain, name="BookDataBinding")
else:
    # Domain class 'Book' not resolved; data binding skipped.
    table_book_0_binding = None
if table_book_0_binding:
    table_book_0.data_binding = table_book_0_binding
ifzdh = Button(
    name="ifzdh",
    description="Button component",
    label="+ decrease_stock",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Book_m_decrease_stock,
    instance_source="table-book-0",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ifzdh",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ decrease_stock", "data-action-type": "run-method", "data-method": "method_rb01uirsh_mjikkmod", "data-instance-source": "table-book-0", "id": "ifzdh", "method-class": "Book", "endpoint": "/book/{book_id}/methods/decrease_stock/", "is-instance-method": "true", "input-parameters": {'qty': {'type': 'int', 'required': True}}, "instance-source": "table-book-0"}
)
ignlq = ViewContainer(
    name="ignlq",
    description=" component",
    view_elements={ifzdh},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ignlq",
    display_order=3,
    custom_attributes={"id": "ignlq"}
)
ignlq_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ignlq.layout = ignlq_layout
iiqcg = ViewContainer(
    name="iiqcg",
    description="main container",
    view_elements={i2s5v, irbyp, table_book_0, ignlq},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iiqcg",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iiqcg"}
)
iiqcg_layout = Layout(flex="1")
iiqcg.layout = iiqcg_layout
igpoh = ViewContainer(
    name="igpoh",
    description=" component",
    view_elements={i6ido, iiqcg},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="igpoh",
    display_order=0,
    custom_attributes={"id": "igpoh"}
)
igpoh_layout = Layout(layout_type=LayoutType.FLEX)
igpoh.layout = igpoh_layout
wrapper.view_elements = {igpoh}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="Library", view_elements=set(), route_path="/library", screen_size="Medium")
wrapper_2.component_id = "page-library-1"
ij079 = Text(
    name="ij079",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ij079",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ij079"}
)
ivonv = Link(
    name="ivonv",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ivonv",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "ivonv"}
)
i6hmj = Link(
    name="i6hmj",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6hmj",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i6hmj"}
)
ihm5s = Link(
    name="ihm5s",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ihm5s",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "ihm5s"}
)
i0cbc = Link(
    name="i0cbc",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i0cbc",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "i0cbc"}
)
izmpx = ViewContainer(
    name="izmpx",
    description=" component",
    view_elements={ivonv, i6hmj, ihm5s, i0cbc},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="izmpx",
    display_order=1,
    custom_attributes={"id": "izmpx"}
)
izmpx_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
izmpx.layout = izmpx_layout
iua3g = Text(
    name="iua3g",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="iua3g",
    display_order=2,
    custom_attributes={"id": "iua3g"}
)
iwxpw = ViewContainer(
    name="iwxpw",
    description="nav container",
    view_elements={ij079, izmpx, iua3g},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iwxpw",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iwxpw"}
)
iwxpw_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iwxpw.layout = iwxpw_layout
ig7c4 = Text(
    name="ig7c4",
    content="Library",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ig7c4",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ig7c4"}
)
ideq2 = Text(
    name="ideq2",
    content="Manage Library data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ideq2",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ideq2"}
)
table_library_1_col_0 = FieldColumn(label="Name", field=Library_name)
table_library_1_col_1 = FieldColumn(label="Web Page", field=Library_web_page)
table_library_1_col_2 = FieldColumn(label="Address", field=Library_address)
table_library_1_col_3 = FieldColumn(label="Telephone", field=Library_telephone)
table_library_1_col_4_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_library_1_col_4 = LookupColumn(label="Books", path=table_library_1_col_4_path, field=Book_title)
table_library_1 = Table(
    name="table_library_1",
    title="Library List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_library_1_col_0, table_library_1_col_1, table_library_1_col_2, table_library_1_col_3, table_library_1_col_4],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-library-1",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Library List", "data-source": "class_06blhjj3h_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'web_page', 'label': 'Web Page', 'columnType': 'field', '_expanded': False}, {'field': 'address', 'label': 'Address', 'columnType': 'field', '_expanded': False}, {'field': 'telephone', 'label': 'Telephone', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-library-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_library_1_binding_domain = None
if domain_model_ref is not None:
    table_library_1_binding_domain = domain_model_ref.get_class_by_name("Library")
if table_library_1_binding_domain:
    table_library_1_binding = DataBinding(domain_concept=table_library_1_binding_domain, name="LibraryDataBinding")
else:
    # Domain class 'Library' not resolved; data binding skipped.
    table_library_1_binding = None
if table_library_1_binding:
    table_library_1.data_binding = table_library_1_binding
igctj = Button(
    name="igctj",
    description="Button component",
    label="+ cheapest_book_by",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Library_m_cheapest_book_by,
    instance_source="table-library-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="igctj",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ cheapest_book_by", "data-action-type": "run-method", "data-method": "35ef5329-889b-40f0-89ce-9836936fd8a9", "data-instance-source": "table-library-1", "id": "igctj", "method-class": "Library", "endpoint": "/library/{library_id}/methods/cheapest_book_by/", "is-instance-method": "true", "input-parameters": {'author': {'type': 'Author', 'required': True, 'input_kind': 'lookup', 'entity': 'Author', 'lookup_field': 'birth'}}, "instance-source": "table-library-1"}
)
iw2sh = ViewContainer(
    name="iw2sh",
    description=" component",
    view_elements={igctj},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="iw2sh",
    display_order=3,
    custom_attributes={"id": "iw2sh"}
)
iw2sh_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
iw2sh.layout = iw2sh_layout
i4x7h = ViewContainer(
    name="i4x7h",
    description="main container",
    view_elements={ig7c4, ideq2, table_library_1, iw2sh},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i4x7h",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i4x7h"}
)
i4x7h_layout = Layout(flex="1")
i4x7h.layout = i4x7h_layout
i72xj = ViewContainer(
    name="i72xj",
    description=" component",
    view_elements={iwxpw, i4x7h},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i72xj",
    display_order=0,
    custom_attributes={"id": "i72xj"}
)
i72xj_layout = Layout(layout_type=LayoutType.FLEX)
i72xj.layout = i72xj_layout
wrapper_2.view_elements = {i72xj}


# Screen: wrapper_3
wrapper_3 = Screen(name="wrapper_3", description="Author", view_elements=set(), route_path="/author", screen_size="Medium")
wrapper_3.component_id = "page-author-2"
ipbdf = Text(
    name="ipbdf",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ipbdf",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ipbdf"}
)
i0bjw = Link(
    name="i0bjw",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i0bjw",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i0bjw"}
)
i6glz = Link(
    name="i6glz",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6glz",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i6glz"}
)
i0cgk = Link(
    name="i0cgk",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i0cgk",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "i0cgk"}
)
iar9y = Link(
    name="iar9y",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iar9y",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "iar9y"}
)
itcei = ViewContainer(
    name="itcei",
    description=" component",
    view_elements={i0bjw, i6glz, i0cgk, iar9y},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="itcei",
    display_order=1,
    custom_attributes={"id": "itcei"}
)
itcei_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
itcei.layout = itcei_layout
ibwxg = Text(
    name="ibwxg",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ibwxg",
    display_order=2,
    custom_attributes={"id": "ibwxg"}
)
ila6f = ViewContainer(
    name="ila6f",
    description="nav container",
    view_elements={ipbdf, itcei, ibwxg},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ila6f",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ila6f"}
)
ila6f_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ila6f.layout = ila6f_layout
iqa6u = Text(
    name="iqa6u",
    content="Author",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iqa6u",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iqa6u"}
)
ipfdx = Text(
    name="ipfdx",
    content="Manage Author data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ipfdx",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ipfdx"}
)
table_author_2_col_0 = FieldColumn(label="Name", field=Author_name)
table_author_2_col_1 = FieldColumn(label="Birth", field=Author_birth)
table_author_2_col_2_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_author_2_col_2 = LookupColumn(label="Books", path=table_author_2_col_2_path, field=Book_title)
table_author_2 = Table(
    name="table_author_2",
    title="Author List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_author_2_col_0, table_author_2_col_1, table_author_2_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-author-2",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Author List", "data-source": "class_d3f0di6lb_mjikkmoe", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'birth', 'label': 'Birth', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-author-2", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_author_2_binding_domain = None
if domain_model_ref is not None:
    table_author_2_binding_domain = domain_model_ref.get_class_by_name("Author")
if table_author_2_binding_domain:
    table_author_2_binding = DataBinding(domain_concept=table_author_2_binding_domain, name="AuthorDataBinding")
else:
    # Domain class 'Author' not resolved; data binding skipped.
    table_author_2_binding = None
if table_author_2_binding:
    table_author_2.data_binding = table_author_2_binding
i7j3y = ViewContainer(
    name="i7j3y",
    description="main container",
    view_elements={iqa6u, ipfdx, table_author_2},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i7j3y",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i7j3y"}
)
i7j3y_layout = Layout(flex="1")
i7j3y.layout = i7j3y_layout
ilz4z = ViewContainer(
    name="ilz4z",
    description=" component",
    view_elements={ila6f, i7j3y},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="ilz4z",
    display_order=0,
    custom_attributes={"id": "ilz4z"}
)
ilz4z_layout = Layout(layout_type=LayoutType.FLEX)
ilz4z.layout = ilz4z_layout
wrapper_3.view_elements = {ilz4z}


# Screen: wrapper_4
wrapper_4 = Screen(name="wrapper_4", description="Publisher", view_elements=set(), route_path="/publisher", screen_size="Medium")
wrapper_4.component_id = "page-publisher-3"
ibqgoh = Text(
    name="ibqgoh",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ibqgoh",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ibqgoh"}
)
i17g6z = Link(
    name="i17g6z",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i17g6z",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i17g6z"}
)
iwf4pm = Link(
    name="iwf4pm",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwf4pm",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "iwf4pm"}
)
iatgkl = Link(
    name="iatgkl",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iatgkl",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "iatgkl"}
)
imj5hx = Link(
    name="imj5hx",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imj5hx",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "imj5hx"}
)
inebcd = ViewContainer(
    name="inebcd",
    description=" component",
    view_elements={i17g6z, iwf4pm, iatgkl, imj5hx},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="inebcd",
    display_order=1,
    custom_attributes={"id": "inebcd"}
)
inebcd_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
inebcd.layout = inebcd_layout
i8zv2f = Text(
    name="i8zv2f",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i8zv2f",
    display_order=2,
    custom_attributes={"id": "i8zv2f"}
)
ibss4 = ViewContainer(
    name="ibss4",
    description="nav container",
    view_elements={ibqgoh, inebcd, i8zv2f},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ibss4",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ibss4"}
)
ibss4_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ibss4.layout = ibss4_layout
ipbgz1 = Text(
    name="ipbgz1",
    content="Publisher",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ipbgz1",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ipbgz1"}
)
iqb9u4 = Text(
    name="iqb9u4",
    content="Manage Publisher data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iqb9u4",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iqb9u4"}
)
table_publisher_3_col_0 = FieldColumn(label="Name", field=Publisher_name)
table_publisher_3_col_1 = FieldColumn(label="Address", field=Publisher_address)
table_publisher_3_col_2 = FieldColumn(label="Telephone", field=Publisher_telephone)
table_publisher_3 = Table(
    name="table_publisher_3",
    title="Publisher List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_publisher_3_col_0, table_publisher_3_col_1, table_publisher_3_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-publisher-3",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Publisher List", "data-source": "class_o32xm5mdp_moil1glk_pd3", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'address', 'label': 'Address', 'columnType': 'field', '_expanded': False}, {'field': 'telephone', 'label': 'Telephone', 'columnType': 'field', '_expanded': False}, {'field': 'Book', 'label': 'Book', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-publisher-3", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_publisher_3_binding_domain = None
if domain_model_ref is not None:
    table_publisher_3_binding_domain = domain_model_ref.get_class_by_name("Publisher")
if table_publisher_3_binding_domain:
    table_publisher_3_binding = DataBinding(domain_concept=table_publisher_3_binding_domain, name="PublisherDataBinding")
else:
    # Domain class 'Publisher' not resolved; data binding skipped.
    table_publisher_3_binding = None
if table_publisher_3_binding:
    table_publisher_3.data_binding = table_publisher_3_binding
i9verg = ViewContainer(
    name="i9verg",
    description="main container",
    view_elements={ipbgz1, iqb9u4, table_publisher_3},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i9verg",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i9verg"}
)
i9verg_layout = Layout(flex="1")
i9verg.layout = i9verg_layout
iexj2 = ViewContainer(
    name="iexj2",
    description=" component",
    view_elements={ibss4, i9verg},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iexj2",
    display_order=0,
    custom_attributes={"id": "iexj2"}
)
iexj2_layout = Layout(layout_type=LayoutType.FLEX)
iexj2.layout = iexj2_layout
wrapper_4.view_elements = {iexj2}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_2, wrapper_3, wrapper_4}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
