---
doc_id: "mta-wiki:4490"
title: "RU/Resource:Editor/EDF"
source_title: "Resource:RU/Editor/EDF"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ARU/Editor/EDF"
revision_id: 47185
language: "en"
categories: ["RU/Resource"]
generated_at: "2026-07-26T16:16:59.354319+00:00"
---

# RU/Resource:Editor/EDF

EDF означает *Editor Definition File* (файл-описание редактора; формат объявлений редактора). EDF'ы являются XML-файлами с расширением .edf, которые описывают специфические элементы, используемые ресурсом: новые типы элементов, которых самих по себе в MTA нет. Образцами служат <spawnpoint> (спавн), <flag> (флаг), <checkpoint> (чекпоинт) и т.д. Они также используются для того, чтобы устанавливать настройки, используемые модами (gamemode), эти настройки находятся под тегом <settings> внутри *meta.xml* ресурса.

## Вступление

Некоторые ресурсы используют специфические элементы карты. Например, мод захвата флага (CTF) скорее всего будет использовать элементы <flag>, которые будут содержать позиции флагов и их принадлежность командам. Когда загружается карта, мод ищет любые элементы <flag> и соответствующе расставляет флаги - например, через создание объекта флага и его коллизии.

Проблема с этими специфическими элементами в том, что в отличие от встроенных в MTA элементов, редактор карт не понимает, что они из себя представляют. Как должен быть визуально представлен собой элемент <flag>? Какие у него есть характеристики? Без передачи редактору этой информации, вы не сможете использовать его для создания таких специфических элементов, и вам придется прибегнуть к ручному редактированию .map-файла через текстовый редактор. К счастью, это необязательно: любой ресурс может содержать editor definition file, который опишет специфические элементы карты, используемые ресурсом.

## Использование definition files в редакторе

Как и описано в [главной инструкции по редактору](https://wiki.multitheftauto.com/wiki/RU/Resource:Editor), чтобы иметь возможность создавать специфические элементы ресурса на вашей карте, вам придется его добавить в окне *Definitions*. Нажмите кнопку *Definitions* в главном меню и дважды щелкните по ресурсу из левого списка. Затем закройте окно и крутаните колесиком мыши в панели элементов, пока не появится желаемый ресурс. С этого момента вы можете создавать и управлять специфическими элементами этого ресурса, как и любым другим элементом.

## Построение EDF-файлов

EDF-файлы - просто XML-файлы с расширением .edf. Начнем с образца: EDF'а мода Capture the Orb.

```
<def name="Capture the Orb">
    <element name="orb" friendlyname="Orb spawnpoint" instructions="Place your orb in a position that can be collected.">
        <data name="position" type="coord3d" default="0,0,0" />
        <marker size="0.5" type="corona" color="#ffff00ff" />
    </element>
    <element name="objective" friendlyname="Objective point" instructions="Place your objective point in a position that can be reached.">
        <data name="position" type="coord3d" default="0,0,0" />
        <marker size="3" type="cylinder" color="#9370dbaa" />
    </element>
    <element name="spawnpoint" friendlyname="Spawnpoint">
        <object editorOnly="true" model="3092" posZ="1" />
        <data name="position" type="coord3d" default="0,0,0" />
        <data name="rotation" type="coord3d" default="0,0,0" />
        <data name="skin" type="skinID" default="0" />
    </element>
</def>
```

Как вы уже убедились, синтаксис очень легок для понимания. Root element (корневой элемент), <def>, содержит несколько <element>. Каждый из этих <element> описывает специфический элемент и задает его имя, визуальное представление и доступные ему настройки.

### Визуальное представление

Каждый child node (дочерний узел) <element>, не являющийся <data>, отвечает за визуальное представление. Объектов, маркеров, пикапов и т.д. могут быть один или несколько. Для каждого элемента вы можете опционально задать позицию (posX, posY, posZ) и угол вращения (rotX, rotY, rotZ): они *родственны* с позицией и вращенем каждого отдельно взятого элемента. На примере Capture the Orb выше, если бы вы захотели создать spawnpoint на (30, 14, 3), редактор бы отобразил объект модели 3092 на координатах (30, 14, 4), потому что posZ объекта, равная 1, была бы сложена с координатой spawnpoint по оси z, равной 3.

### Настройки

Настройки специфического элемента описаны в <data>. Имена некоторых настроек, такие как *position* и *rotation*, особенные: они могут быть изменены при перемещении и вращении элемента прямо в редакторе. Другие настройки могут быть изменены в окне Properties.

### Визуальное представление, зависимое от настроек

Специфический элемент можно сделать зависимым от одной или более настроек другого элемента. Например, элемент <checkpoint> race мода, содержащий <marker>: checkpoint имеет несколько атрибутов, таких как color и size, которые должны быть отражены и в marker. Чтобы это сделать, укажите какой-либо из-них в виде *!propertyname!* в качестве как одного или более атрибутов зависимого элемента. Например:

```
<def name="Race">
	<element name="checkpoint" friendlyname="Race checkpoint">
		<data name="position" type="coord3d" required="true" default="0,0,0" />

		<data name="type" type="selection:checkpoint,ring" required="true" default="checkpoint" />
		<data name="size" type="number" required="true" default="2.25"/>
		<data name="color" type="color" required="false" default="#ff0000ff" />
		...
		
		<marker type="!type!" size="!size!" color="!color!" />
	</element>
</def>
```

Теперь, когда бы настройки checkpoint "type", "size" или "color" не менялись, новое значение будет также скопировано в его marker, в связи с чем их внешний вид будет меняться вместе.

### Интеграция в ресурсы

Когда вы написали свой EDF, сохраните его как .edf-файл в папке своего ресурса и добавьте атрибут "edf:definition" в тег <info> meta.xml, как здесь:

```
<meta>
    <info author="erorr404" type="gamemode" ... edf:definition="cto.edf" />
    ...
</meta>
```

## EDF ссылки

### Вшитые элементы

Эти элементы могут использоваться для ваших специфических элементов, вкупе с их настройками.

| <blip> |  |
| --- | --- |
| Атрибут | Тип |
| position | coord3d |
| icon | blipID |
| size | integer |
| color | color |
| dimension | integer |

| <marker> |  |
| --- | --- |
| Атрибут | Тип |
| position | coord3d |
| type | markerType |
| size | number |
| color | color |
| interior | integer |
| dimension | integer |

| <object> |  |
| --- | --- |
| Атрибут | Тип |
| model | objectID |
| position | coord3d |
| rotation | coord3d |
| interior | integer |
| dimension | integer |

| <ped> |  |
| --- | --- |
| Атрибут | Тип |
| position | coord3d |
| model | skinID |
| rotZ | number |
| interior | integer |
| dimension | integer |

| <pickup> |  |
| --- | --- |
| Атрибут | Тип |
| position | coord3d |
| type | pickupType |
| amount | number |
| respawn | integer |
| interior | integer |
| dimension | integer |

| <vehicle> |  |
| --- | --- |
| Атрибут | Тип |
| model | vehicleID |
| position | coord3d |
| rotation | coord3d |
| color | vehiclecolors |
| upgrades | vehicleupgrades |
| plate | plate |
| interior | integer |
| dimension | integer |

| <radararea> |  |
| --- | --- |
| Атрибут | Тип |
| posX | number |
| posY | number |
| sizeX | number |
| sizeY | number |
| color | color |
| dimension | integer |

### Вшитые названия настроек

Настройки с данными именами особенно воспринимаются редактором и могут быть изменены не только через окно Properties.

| Название | Тип |
| --- | --- |
| position | coord3d |
| rotation | coord3d |

### Типы настроек

Это -  типы, которые могут быть выбранными в (<data>) ваших специфических элементов.

#### Типы

| Название | Описание | Значение |
| --- | --- | --- |
| boolean | Простое двоичное (булевое) значение. | "true" или "false" |
| natural | Натуральное число (целое и неотрицательное). |  |
| integer | Целое число. |  |
| number | Рациональное число. |  |
| string | Простая текстовая строка. |  |
| color | цвет, с или без указания прозрачности (alpha). | #RRGGBB или #RRGGBBAA |

#### Координаты

| Название | Описание | Значение |
| --- | --- | --- |
| camera | Позиция и угол обзора камеры. | posX,posY,posZ,lookatX,lookatY,lookatZ |
| coord3d | 3-компонентный вектор, зачастую используемый для позиции и вращения. | x,y,z |

#### Транспорт

| Название | Описание | Значение |
| --- | --- | --- |
| plate | Текст номерного знака для транспортного средства. |  |
| vehiclecolors | цвета транспортного средства | colorID1,colorID2,colorID3,colorID4 |
| vehicleupgrades | апгрейды (тюнинг) транспортного средства | upgradeID1,upgradeID2,... |

#### ID моделей

| Название | Описание | Значение |
| --- | --- | --- |
| blipID | ID картинки для метки |  |
| objectID | ID модели для объекта |  |
| pickupType | Броня, хп или оружие | "armor", "health" или ID-номер оружия |
| skinID | ID скина для педа |  |
| vehicleID | ID модели для транспортного средства |  |
| weaponID | Оружие, напр. M4 | ID-номер оружия, напр. 31 |

#### Колшейпы и маркеры

| Название | Описание | Значение |
| --- | --- | --- |
| colshapeType | коллизионные круг, куб, прямоугольник, сфера или труба | Один из: "colcircle", "colcube", "colrectangle", "colsphere", "coltube" |
| markerType | Стрелка, чекпоинт, кольцо, цилиндр или круглый маркер. | Один из: "arrow", "checkpoint", "corona", "cylinder", "ring" |

#### Специальные

| Название | Описание | Значение |
| --- | --- | --- |
| element:type | Элемент определенного типа, например: element:flag | ID элемента |
| selection:val1,val2,... | Показывает выпадающий список, из которого можно выбрать одно из значений. | Выборное значение |
