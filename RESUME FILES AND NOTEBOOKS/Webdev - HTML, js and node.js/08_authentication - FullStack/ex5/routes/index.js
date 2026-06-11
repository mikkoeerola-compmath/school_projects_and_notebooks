const express=require('express');
const router=express.Router();

// Home route
router.get('/', (req, res) => {
  const pageTitle = "users API";
  res.send(`Welcome to ${pageTitle}. You can query for user data at the /users and /users/:id endpoints`);
});

module.exports = router;
