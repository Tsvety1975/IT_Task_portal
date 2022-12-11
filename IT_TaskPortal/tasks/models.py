from enum import Enum

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from IT_TaskPortal.accounts.models import Department
from IT_TaskPortal.accounts.validators import validate_only_digits
from IT_TaskPortal.team.models import Employees

UserModel = get_user_model()


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class StateOfTask(ChoicesEnumMixin, Enum):
    open = 'Нов'
    in_progress = 'В прогрес'
    pending = 'Очаква изпълнение'
    partial_executed = 'Частично изпълненa'
    close = 'Приключена'


class YesOrNo(ChoicesEnumMixin, Enum):
    yes = 'да/yes'
    no = 'не/no'

class ReadWrite(ChoicesEnumMixin, Enum):
    read_only = 'без право да записва/without right to write'
    write_read = 'може да прави записи /can write in directory'
# Create your models here.
#
class Buildings(models.Model):
    building_name = models.CharField(
        max_length=40,
    )
    drawing_file = models.FileField(
        upload_to='drawings',
        blank=True,
    )


    def __str__(self):
        return self.building_name


class TaskForNewWorker(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        verbose_name="Създал заявката | Request created by",
    )

    is_new_worker = models.BooleanField(

        verbose_name='Служителят е нов потребител | New user',
        blank=True,

    )

    worker_first_name_bg = models.CharField(
        max_length=30,
        verbose_name="Име на кирилица| First name",
    )

    worker_second_name_bg = models.CharField(
        max_length=30,
        verbose_name="Бащино име кирилица| Second name",
       null=True,
    )

    worker_last_name_bg = models.CharField(
        max_length=30,
        verbose_name="Фамилия на кирилица| Family name",
    )

    worker_first_name_en = models.CharField(
        max_length=30,
        verbose_name="Име на латиница| First name",
    )

    worker_last_name_en = models.CharField(
        max_length=30,
        verbose_name="Фамилия на латиница| Family name",
    )

    worker_from_data = models.DateField(
        verbose_name="Дата на постъпване| Data of entry",
    )

    worker_department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name="Дирекция| Department",
        null=True,
    )

    worker_division = models.CharField(
        max_length=40,
        verbose_name="Отдел| Division",
    )

    worker_position = models.CharField(
        max_length=50,
        verbose_name="Длъжност| Position",
    )

    worker_phone_number = models.CharField(
        max_length=10,
        validators=(
            validators.MinLengthValidator(9),
            validate_only_digits,

        ),
        verbose_name="Мобилен или стационарен  телефонен номер| Mobile or work number",
    )

    work_place_building = models.ForeignKey(
        Buildings,
        on_delete=models.SET_NULL,
        verbose_name="Изберете сградата в която работите| Choose workplace building",
        null=True,
    )

    office_number = models.CharField(
        max_length=50,
        verbose_name="Помещение| Room",
    )

    rights_same_as_worker_name = models.CharField(
        max_length=180,
        blank=True,
        verbose_name="Права сходни със служител(Достъп до фирмени ресурси/папки| Rights similar to :(access to folders)",
    )

    access_to_read_write = models.CharField(
        max_length=12,
        choices=ReadWrite.choices(),
        verbose_name='Права само за четене-записване | Rights to read-write',
        blank=True,
        null=True,

    )



    # Services
    create_user_account = models.BooleanField(
        verbose_name="Създаване на нов потребител в системата| Create new User account",
    )
    create_user_email = models.BooleanField(
        verbose_name="Електронна поща | Email",
        blank=True,

    )

    access_to_group_mail = models.EmailField(
        verbose_name='Достъп но групов имейл | Join to email group',
        blank=True,
    )

    vpn_from_work_laptop = models.BooleanField(

        verbose_name="Отдалечен достъп до фирмената мрежа от служебен лаптоп| VPN from work laptop",
    )
    vpn_from_private_comp_to_office_com = models.BooleanField(
        verbose_name="Отдалечен достъп до фирмената мрежа oт личен компютър | VPN from private to work domain system"
    )
    # internet_access = models.BooleanField(
    #     verbose_name="Интернет| Internet",

    # ) # Technical equipment

    computer = models.BooleanField(
        verbose_name="Настолен компютър| Desktop computer",
    )
    laptop = models.BooleanField(
        verbose_name="Лаптоп| Laptop",
    )

    monitor=models.BooleanField(
        verbose_name='Монитор | Monitor',
        blank=True,
        default=False,

    )

    # Printers and scanners
    laser_printer_scanner = models.BooleanField(
        verbose_name="Черно-бял печат| Black and White Printer",
    )

    scaner = models.BooleanField(
        verbose_name="Скенер| Scanner",
        blank=True,
        default=False,

    )

    matrix_printer = models.BooleanField(
        verbose_name="Матричен принтер| Matrix printer",
    )
    color_printing_possibility = models.BooleanField(
        verbose_name="Цветно отпечатване| Color print",
    )
    color_copy_possibility = models.BooleanField(
        verbose_name="Цветно копиране| Color copy",
        blank=True,
        default=False,


    )

    # Software
    microsoft_office = models.BooleanField(
        verbose_name="Microsoft Office",
    )
    eventis = models.BooleanField(
        verbose_name="Eventis",
    )
    sonita = models.BooleanField(
        verbose_name="SioPro",
    )

    sonita_bi = models.BooleanField(
        verbose_name="SioProBI",
        default=False,
        blank=True,
    )

    ahm = models.BooleanField(
        verbose_name="Полетна информация| AHM",
    )
    omeks = models.BooleanField(
        verbose_name="Omeks",
    )

    fuels = models.BooleanField(
        verbose_name="Fuels",
        default=False,
    )

    avtoservice = models.BooleanField(
        verbose_name="Avtoservice",
        default=False,

    )

    procurement_software = models.BooleanField(
        verbose_name="Софтуер за поръчки| Software for procurement",
    )
    legal_software = models.BooleanField(
        verbose_name="Lakorda",
    )

    adobe_software = models.BooleanField(
        verbose_name="adobe Pro",
        default=False,
    )

    deepl = models.BooleanField(
        verbose_name="Deepl",
        default=False,
    )

    nanocad = models.BooleanField(
        verbose_name="NanoCad",
        default=False,

    )

    # telecommunication equipment
    landline_phone = models.BooleanField(
        verbose_name="Стационарен телефон| Stationary Phone",
    )
    dekt_mobile_phone = models.BooleanField(
        verbose_name="Дект| Dect",
    )
    mobile_phone = models.BooleanField(
        verbose_name="Мобилен телефон| Mobile phone",
    )
    tetra_station = models.BooleanField(
        verbose_name="Тетра станция| Tetra",
    )
    employee_responsible = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Отговорно лице| Person responsible",

    )
    # To deside how to put mani responsible persons
    # employee_first_responsible = models.ForeignKey(
    #     Employees,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     verbose_name="Втови отговорник | Person responsible",
    #
    # )
    # employee_second_responsible = models.ForeignKey(
    #     Employees,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     verbose_name="Отговорно лице за техническа поддръжка| Person responsible",

    # )

    remarks = models.TextField(
        max_length=200,
        blank=True,
        verbose_name="Коментар | Remarks",
    )
    status = models.CharField(
        choices=StateOfTask.choices(),
        max_length=50,
        default='Очаква изпълнение',
        verbose_name="Статус| State",
    )
    data_of_creation = models.DateField(
        auto_now=True,
        verbose_name="Дата на създаване| Data_of_creation",
    )

    data_of_partial_finish = models.DateField(
        verbose_name='Дата на частично изпълнение',
        blank=True,
        null=True,
    )

    data_of_execution = models.DateField(
        null=True,
        verbose_name="Дата на приключване| Data of execution",
        blank=True,
    )


class TelecomContract(models.Model):
    contract_number = models.CharField(
        max_length=20,
        verbose_name='Номер на договор',
    )
    contractor_name = models.CharField(
        max_length=50,
        verbose_name="Име на фирма",
    )
    contractor_bulstat = models.CharField(
        max_length=20,
        blank=True,
    )

    person_for_contact = models.CharField(
        max_length=60,
        verbose_name="Лице за контакт",
        blank=True,
    )

    contractor_email = models.EmailField(
        verbose_name='Email за контакт',
        blank=True,
    )
    contractor_phone = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Телефон на лице за контакт',
    )

    data_from = models.DateField(
        verbose_name='Начална дата на договора',
    )
    end_data_of_contract = models.DateField(
        verbose_name='Дата на изтичане на договора',)

    person_involved = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Отговорно лице| Person responsible",
    )

    description = models.CharField(
        max_length=300,
        verbose_name='Предмет на договора',
    )

    contract_file = models.FileField(
        upload_to='telecom/contracts',
        blank=True,
    )

    anex_one = models.CharField(
        max_length=20,
        blank=True,
    )

    anex_one_file = models.FileField(
        upload_to='telecom/anex',
        blank=True,
    )

    anex_two= models.CharField(
        max_length=20,
        blank=True,
    )

    anex_two_file = models.FileField(
        upload_to='telecom/anex',
        blank=True,
    )

    anex_three = models.CharField(
        max_length=20,
        blank=True,
    )
    anex_three_file = models.FileField(
        upload_to='telecom/anex',
        blank=True,
    )

    prise_contract = models.CharField(
        max_length=6,
        blank=True,
    )
    prise_last_anex = models.CharField(
        max_length=6,
        blank=True,
    )


class ExternalTelekomTasks(models.Model):
    data_of_creation = models.DateField(
        auto_now=True,
        verbose_name="Дата на създаване| Data_of_creation",
    )
    contractor_name= models.CharField(
        max_length=50,
        verbose_name='Име на фирма подател',
    )

    for_contract = models.ForeignKey(
        TelecomContract,
        on_delete=models.SET_NULL,
        verbose_name='Към договор',
        blank=True,
        null=True,

    )

    request_paper = models.FileField(
        upload_to='telecom/request_papers',
        blank=True,
    )

    place_building = models.ForeignKey(
        Buildings,
        on_delete=models.SET_NULL,
        verbose_name="Сграда",
        null=True,
        blank=True,
    )

    office_descropton = models.CharField(
        max_length=50,
        verbose_name="Помещение| Room",
        blank=True,

    )

    protocol_for_execution = models.FileField(
        upload_to='protocols',
        blank=True,
    )
    # servisese required

    new_access_points = models.BooleanField(
        verbose_name="Точки за достъп",
    )
    point_number = models.IntegerField(
        blank=True,
        verbose_name='Брой точки',
    )

    data_of_execution = models.DateField(
        verbose_name='Дата на изпълнение',
        blank=True,
        null=True,
    )

    responsible_employee = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Отговорно лице| Person responsible",
    )

    remarks_from_executor = models.TextField(
        max_length=300,
        blank=True,
        verbose_name="Коментар по изпълнението",
    )