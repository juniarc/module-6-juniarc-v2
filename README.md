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
    "gender": "Female",
    "name": "Unta",
    "special_req": "None",
    "species": "Cat"
}
```

##### Responses

```
{
    "message": "Success add new animal"
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
    "species": "Dog",
    "age": 2,
    "gender": "Male",
    "special_req": ""
}
```

##### Responses

```
{
    "age": 2,
    "gender": "Male",
    "id": 1,
    "name": "Ujang",
    "special_req": "None",
    "species": "Dog"
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
    "message": "Success add new employee"
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
    "end_schedule": "31-10-2024 14:30:00",
    "id": 1,
    "name": "Ayat",
    "role": "Casheer",
    "start_schedule": "30-10-2024 14:30:00"
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