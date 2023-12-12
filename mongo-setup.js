rsconf = {
  _id : "rs0",
  members: [
      {
          "_id": 0,
          "host": "mongodb1:27011",
          "priority": 3
      }
  ]
}

rs.initiate(rsconf);