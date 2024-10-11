# Assignment Module 6

### Base Url
```
https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/
```

## Animals

### Get All Animals

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/animals</code></summary>

##### Responses

```
[
    {
        "age": 1,
        "enclosure_id": 1,
        "gender": "Female",
        "id": 1,
        "name": "Onyet",
        "special_req": "None",
        "species": "Cat"
    }
]
```
</details>

### Get Animal by Id

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/animals/:id</code></summary>

##### Parameters

id (Number)

##### Responses

```
{
    "age": 1,
    "gender": "Female",
    "enclosure_id": 1,
    "id": 1,
    "name": "Onyet",
    "special_req": "None",
    "species": "Cat"
}
```
</details>

### Add New Animal

<details>
 <summary><code>POST</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/animals/</code></summary>


##### Body

```
{
    "age": 1,
    "enclosure_id": 1,
    "gender": "Female",
    "name": "Unta",
    "special_req": "None",
    "species": "Cat"
}
```

##### Responses

```
{
    'message' : 'Success add new animal',
    'animals': {
        "age": 1,
        "enclosure_id": 1,
        "gender": "Female",
        "id": 1,
        "name": "Onyet",
        "special_req": "None",
        "species": "Cat"
    }
}
```
</details>

### Edit Animal by Id

<details>
 <summary><code>PUT</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/animals/:id</code></summary>


##### Parameter

id (number)

##### Body

```
{
	"name": "Ujang",
    "enclosure_id": 1,
    "species": "Dog",
    "age": 2,
    "gender": "Male",
    "special_req": ""
}
```

##### Responses

```
{
    'message' : 'Success update animal',
    'animals': {
        "age": 1,
        "enclosure_id": 1,
        "gender": "Female",
        "id": 1,
        "name": "Onyet",
        "special_req": "None",
        "species": "Cat"
    }
}
```
</details>

### Delete Animal by Id

<details>
 <summary><code>DELETE</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/animals/:id</code></summary>


##### Parameter

id (number)

##### Responses

```
{
    "message": "Success delete animal"
}
```
</details>


## Employees

### Get All Employees

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/employees</code></summary>

##### Responses

```
[
    {
        "end_schedule": "31-10-2024 14:30:00",
        "id": 1,
        "name": "Mahmud",
        "role": "Zookeper",
        "start_schedule": "30-10-2024 14:30:00"
    },
    {
        "end_schedule": "31-10-2024 14:30:00",
        "id": 2,
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }
]
```
</details>

### Get Employee by Id

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/employees/:id</code></summary>

##### Parameters

id (Number)

##### Responses

```
{
    "end_schedule": "31-10-2024 14:30:00",
    "id": 1,
    "name": "Mahmud",
    "role": "Zookeper",
    "start_schedule": "30-10-2024 14:30:00"
}
```
</details>


### Add New Employee

<details>
 <summary><code>POST</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/employees</code></summary>


##### Body

```
{
    "end_schedule": "31-10-2024 14:30:00",
    "name": "Halim",
    "role": "Casheer",
    "start_schedule": "30-10-2024 14:30:00"
}
```

##### Responses

```
{
    "message": "Success add new employee",
    "employees": {
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00" 
    }
}
```
</details>

### Edit Employee by Id

<details>
 <summary><code>PUT</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/employees/:id</code></summary>


##### Parameter

id (number)

##### Body

```
{
    "end_schedule": "31-10-2024 14:30:00",
    "name": "Ayat",
    "role": "Casheer",
    "start_schedule": "30-10-2024 14:30:00"
}
```

##### Responses

```
{
    "message": "Success edit employee",
    "employees": {
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00" 
    }
}
```
</details>


### Delete Employee by Id

<details>
 <summary><code>DELETE</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/employees/:id</code></summary>


##### Parameter

id (number)

##### Responses

```
{
    "message": "Success delete employee"
}
```
</details>


## Visitors

### Get All Visitors

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors</code></summary>

##### Responses

```
[
    {
        "date": "30-10-2024 14:30:00",
        "event_type": "Normal day",
        "feedback": "Positive",
        "id": 2,
        "ticket_type": "Adult"
    },
    {
        "date": "31-10-2024 14:30:00",
        "event_type": "Weekend day",
        "feedback": "Positive",
        "id": 3,
        "ticket_type": "Adult"
    },
    {
        "date": "31-10-2024 14:30:00",
        "event_type": "Normal day",
        "feedback": "Positive",
        "id": 4,
        "ticket_type": "Child"
    },
    {
        "date": "31-10-2024 14:30:00",
        "event_type": "Weekend day",
        "feedback": "Positive",
        "id": 5,
        "ticket_type": "Child"
    }
]
```
</details>

### Get Visitors by Id

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors/:id</code></summary>

##### Parameters

id (Number)

##### Responses

```
{
    "date": "30-10-2024 14:30:00",
    "event_type": "Normal day",
    "feedback": "Positive",
    "id": 2,
    "ticket_type": "Adult"
}
```
</details>

### Add New Visitor

<details>
 <summary><code>POST</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors</code></summary>


##### Body

```
{
    "date": "30-10-2024 14:30:00",
    "event_type": "Normal day",
    "feedback": "Positive",
    "ticket_type": "Adult"
}
```

##### Responses

```
{
    "message": "Success add new visitor",
    "employees": {
        "date": "30-10-2024 14:30:00",
        "event_type": "Normal day",
        "feedback": "Positive",
        "id": 2,
        "ticket_type": "Adult"
    }
}
```
</details>

### Edit Visitor by Id

<details>
 <summary><code>PUT</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors/:id</code></summary>


##### Parameter

id (number)

##### Body

```
{
    "date": "30-10-2024 14:30:00",
    "event_type": "Normal day",
    "feedback": "Positive",
    "ticket_type": "Adult"
}
```

##### Responses

```
{
    "message": "Success edit visitor",
    "employees": {
        "date": "30-10-2024 14:30:00",
        "event_type": "Normal day",
        "feedback": "Positive",
        "id": 2,
        "ticket_type": "Adult"
    }
}
```
</details>

### Delete Visitor by Id

<details>
 <summary><code>DELETE</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors/:id</code></summary>


##### Parameter

id (number)

##### Responses

```
{
    "message": "Success delete visitor"
}
```
</details>



## Enclosures

### Get All Enclosures

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/enclosures</code></summary>

##### Responses

```
[
    {
        "id": 4,
        "location": "Zona 1",
        "name": "Kandang 1"
    },
    {
        "id": 5,
        "location": "Zona 1",
        "name": "Kandang Anjing"
    }
]
```
</details>

### Get Visitors by Id

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/visitors/:id</code></summary>

##### Parameters

id (Number)

##### Responses

```
{
    "date": "30-10-2024 14:30:00",
    "event_type": "Normal day",
    "feedback": "Positive",
    "id": 2,
    "ticket_type": "Adult"
}
```
</details>

### Add New Enclosure

<details>
 <summary><code>POST</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/enclosures</code></summary>


##### Body

```
{
    "location": "Zona 1",
    "name": "Kandang Anjing"
}
```

##### Responses

```
{   
    "message": "Success add new enclosure",
    "enclosures": {
        "id": 7,
        "location": "Zona 1",
        "name": "Kandang Anjing"
    },
}
```
</details>

### Edit Enclosure by Id

<details>
 <summary><code>PUT</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/enclosures/:id</code></summary>


##### Parameter

id (number)

##### Body

```
{
    "location": "Zona 1",
    "name": "Kandang Anjing"
}
```

##### Responses

```
{
    "message": "Success update enclosure",
    "enclosures": {
        "id": 7,
        "location": "Zona 1",
        "name": "Kandang 2"
    }
}
```
</details>

### Delete Enclosure by Id

<details>
 <summary><code>DELETE</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/enclosure/:id</code></summary>


##### Parameter

id (number)

##### Responses

```
{
    "message": "Success delete enclosure"
}
```
</details>



## Feedings

### Get All Feedings

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/feedings</code></summary>

##### Responses

```
[
    {
        "animal_id": 1,
        "enclosure_id": 1,
        "feeding_time": "30-10-2024 14:30:00",
        "food_type": "Wishkas",
        "id": 2,
        "reminder": "30-10-2024 12:30:00"
    },
    {
        "animal_id": 1,
        "enclosure_id": 1,
        "feeding_time": "30-10-2024 14:30:00",
        "food_type": "Wishkas",
        "id": 3,
        "reminder": "30-10-2024 12:30:00"
    }
]
```
</details>

### Get Feeding by Id

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/feedings/:id</code></summary>

##### Parameters

id (Number)

##### Responses

```
{
    "animal_id": 1,
    "enclosure_id": 1,
    "feeding_time": "30-10-2024 14:30:00",
    "food_type": "Wishkas",
    "id": 2,
    "reminder": "30-10-2024 12:30:00"
}
```
</details>

### Add New Feeding

<details>
 <summary><code>POST</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/feedings</code></summary>


##### Body

```
{
    "animal_id": 29,
    "enclosure_id": 5,
    "food_type": "Wishkas",
    "feeding_time": "30-10-2024 14:30:00",
    "reminder": "30-10-2024 12:30:00"
}
```

##### Responses

```
{   
    "message": "Success add new feeding time",
    "feeding": {
        "animal_id": 29,
        "enclosure_id": 5,
        "feeding_time": "30-10-2024 14:30:00",
        "food_type": "Wishkas",
        "id": 4,
        "reminder": "30-10-2024 12:30:00"
    },
}
```
</details>

### Edit Feeding by Id

<details>
 <summary><code>PUT</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/feedings/:id</code></summary>


##### Parameter

id (number)

##### Body

```
{
    "animal_id": 29,
    "enclosure_id": 5,
    "feeding_time": "30-10-2024 14:30:00",
    "food_type": "Wishkas",
    "id": 2,
    "reminder": "30-10-2024 12:30:00"
}
```

##### Responses

```
{   
    "message": "Success update feeding time"
    "feeding": {
        "animal_id": 29,
        "enclosure_id": 5,
        "feeding_time": "30-10-2024 14:30:00",
        "food_type": "Wishkas",
        "id": 2,
        "reminder": "30-10-2024 12:30:00"
    },
}
```
</details>

### Delete Feeding by Id

<details>
 <summary><code>DELETE</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/feedings/:id</code></summary>


##### Parameter

id (number)

##### Responses

```
{
    "message": "Success delete feeding time"
}
```
</details>


## Reports

### Get All Animal Report

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/reports/animal</code></summary>

##### Responses

```
[
    {
        "count": 1,
        "enclosure_id": 5,
        "gender": "Male",
        "species": "Dog"
    },
    {
        "count": 1,
        "enclosure_id": 4,
        "gender": "Female",
        "species": "Cat"
    },
    {
        "count": 1,
        "enclosure_id": 4,
        "gender": "Male",
        "species": "Cat"
    }
]
```
</details>

### Get Visitors Report

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/reports/visitors</code></summary>

##### Responses

```
[
    {
        "count": 1,
        "date": "31-10-2024 14:30:00",
        "event_type": "Weekend day",
        "feedback": "Positive",
        "ticket_type": "Adult"
    },
    {
        "count": 1,
        "date": "30-10-2024 14:30:00",
        "event_type": "Normal day",
        "feedback": "Positive",
        "ticket_type": "Adult"
    },
    {
        "count": 2,
        "date": "31-10-2024 14:30:00",
        "event_type": "Weekend day",
        "feedback": "Positive",
        "ticket_type": "Child"
    }
]
```
</details>

### Get Revenue Report

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>https://urgent-gwenni-juniarc-caaccaf6.koyeb.app/reports/revenue</code></summary>

##### Responses

```
[
    {
        "event_type": "Weekend day",
        "revenue": 50,
        "ticket_type": "Adult"
    },
    {
        "event_type": "Normal day",
        "revenue": 30,
        "ticket_type": "Adult"
    },
    {
        "event_type": "Weekend day",
        "revenue": 50,
        "ticket_type": "Child"
    }
]
```
</details>
