const express = require('express');
const cors = require('cors');
const pg = require('pg')

const Pool = require('pg').Pool
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'test1',
  password: '1234',
  port: 5432,
})

const app = express()

const getData = (request, response) => {
    const id = parseInt(request.params.id)
  
    pool.query('SELECT * FROM public.test1',  (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).json(results.rows)
    })
  }

const getDataOne = (request, response) => {
    const id = request.params.id
  
    pool.query('SELECT * FROM public.fakeGPS WHERE "nodeName" = $1',[id],  (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).json(results.rows)
    })
  }

  app.use(cors())

app.get('/', (req,res)=>{
    res.send({"name":"ongseongwoo"})
})

app.get('/getdata',getData)

app.get('/data/:id',getDataOne)
app.listen(5000,'127.0.0.1', ()=>{
    console.log('App run at 5000')
})