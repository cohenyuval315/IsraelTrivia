// AuthService.js

const API_URL = 'http://your-api-url.com'; // Replace with your actual API URL

const _request = async (method,endpoint, body = null) => {
  const requestOptions = {
    method: method,
    headers: {
      'Content-Type': 'application/json'
    },
  };

  // Include the body in the request options if it's provided
  if (body !== null) {
    requestOptions.body = JSON.stringify(body);
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, requestOptions);
    const data = await response.json();
    if (response.ok) {
      return data; // This will be an object that contains the response data from the server
    } else {
      throw new Error(data.message || 'An error occurred during the request.');
    }
  } catch (error) {
    console.error(error.message);
    throw error; // Re-throw the error so the calling function can handle it
  }
};


const handleLogin = async (username, password) => {
    try {
      // Call the postRequest function with the login endpoint and the user credentials
      const data = await _request('POST','/auth/login', { username, password });
  
      // If the request was successful, the response data should contain the token
      const user_id = data['user_id'];
  
    
      // Return the user id for further use
      return user_id;
    } catch (error) {
      // If an error occurs, log it or handle it as needed
      console.error('Login failed:', error);
      throw error;
    }
  };
  
  // Usage:
  try {
    const userToken = await login('myUsername', 'myPassword');
    console.log('User ID received:', userToken);
    } catch (error) {
    console.error('Login error:', error);
  }
  const handleLogout = async (user_id) => {
    try {
      // Construct the endpoint for logout
      const endpoint = '/auth/logout';
  
      // Call the _request function with a POST method, endpoint, and token
      // Assuming your API requires a token to be sent for logging out
      const data = await _request('POST', endpoint, { token });
  
      // Handle the response data as needed
      console.log('Logout successful:', data);
  
      // Additional client-side cleanup can be performed here
      // Like removing the token from storage or resetting app state
      // localStorage.removeItem('token');
  
      return data;
    } catch (error) {
      // If an error occurs, log it or handle it as needed
      console.error('Logout failed:', error);
      throw error; // Re-throw the error to be handled by the calling code
    }
  };
  
  // Usage:
  try {
    const user_id = 'your_user_token'; // Replace with actual token
    await logout(user_id);
    console.log('User logged out successfully');
    // Here you might redirect the user to the login screen or perform other UI updates
  } catch (error) {
    console.error('Error during logout:', error);
  }
  
  
  const handleRegister = async (username, password) => {
    try {
      // Assuming _request is a previously defined function similar to postRequest for making API calls
      const data = await _request('POST', '/auth/register', {
        username,
        password
      });
  
      // If the request was successful, the response data should contain the user_id or a success message
      const user_id = data['user_id'];
  
      // Return the user_id for further use
      return user_id;
    } catch (error) {
      // If an error occurs, log it or handle it as needed
      console.error('Registration failed:', error);
      throw error; // Re-throw the error to be handled by the calling code
    }
  };
  
  // Usage:
  try {
    // Replace 'additionalData' with actual fields required by your registration process
    const userId = await handleRegister('newUsername', 'newPassword', { email: 'user@example.com' });
    console.log('User registered with ID:', userId);
    // Proceed with the newly registered user ID as needed
  } catch (error) {
    // Handle the registration error - show an error message to the user, etc.
    console.error('Registration error:', error);
  }
    
  const updateUserProgress = async (userId, level_id, level_index, score) => {
    try {
      const newProgress = {
        "level_id" : level_id,
        "level_index" : level_index,
        "score" : score
      }  
      // Construct the endpoint with the user ID
      const endpoint = `/users`;
  
      // Call the _request function with the PUT method, endpoint, and new progress data
      const data = await _request('PUT', endpoint, newProgress);
  
      // Handle the response data as needed
      console.log('Progress updated:', data);
        
      // Return the response data for further use
      return data;
    } catch (error) {
      // If an error occurs, log it or handle it as needed
      console.error('Update failed:', error);
      throw error; // Re-throw the error to be handled by the calling code
    }
  };
  
  // Usage:
  try {
    const userId = '123'; // Replace with actual user ID
    const newProgress = { level: 10, score: 200 }; // Replace with actual progress data
    await updateUserProgress(userId, newProgress);
    console.log('User progress updated successfully');
  } catch (error) {
    console.error('Error updating user progress:', error);
  }
  
  const getLevelStatement = async (userId) => {
    try {
      // Construct the endpoint with the user ID, assuming an endpoint like '/users/:userId/level'
      const endpoint = `/api/statements`;
  
      // Call the _request function with a GET method and the endpoint
      // Since it's a GET request, there's no need to provide a body
      const data = await _request('GET', endpoint);
  
      // Handle the response data as needed
      console.log('Level data:', data);
  
      // Return the response data for further use
      return data;
    } catch (error) {
      // If an error occurs, log it or handle it as needed
      console.error('Error fetching level statement:', error);
      throw error; // Re-throw the error to be handled by the calling code
    }
  };
  
  // Usage:
  try {
    const userId = '123'; // Replace with actual user ID
    const levelData = await getLevelStatement(userId);
    console.log('User level data:', levelData);
  } catch (error) {
    console.error('Error in getting level data:', error);
  }
  