// AuthService.js

class ApiClient {
  constructor(){
    this.base_url = 'http://172.20.27.195:5000'
    this.user_id = "0"
  }
  

  _request = async (method,endpoint, body = null) => {
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
      const response = await fetch(`${this.base_url}${endpoint}`, requestOptions);
      const data = await response.json();
      if (response.ok) {
        return data; // This will be an object that contains the response data from the server
      } else {
        console.error(`Request failed with status ${response.status}: ${data.message}`);
      
        throw new Error(data.message || 'An error occurred during the request.');
      }
    } catch (error) {
      console.error(error.message);
      throw error; // Re-throw the error so the calling function can handle it
    }
  }

  getAppData = async () => {
    const endpoint = `/appdata`;
    const data = await this._request('GET', endpoint);
    return data;
  }

  getUserProfile = async () => {
    const endpoint = `/user`;
    const reqBody = {
      "user_id":this.user_id
    }

    const data = await this._request('POST', endpoint, reqBody);
    return data
  }

  updateUserProgress = async ( level_id, level_index, score) => {
    const newProgress = {
      "user_id":this.user_id,
      "level_id" : level_id,
      "level_index" : level_index,
      "score" : score
    }  
    // const requestOptions = {
    //   method: 'PUT',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify(newProgress)
    // };
  

      const endpoint = `/user`;
      const data = await this._request('PUT', endpoint, newProgress);
      return data
  };

  handleLogin = async (username, password) => {
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

  handleLogout = async (user_id) => {
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

  handleRegister = async (username, password) => {
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

  getLevelStatements = async (level_id) => {      
    const endpoint = `/statements`;
    const body = {
      "level_id" : level_id
    }
      const data = await this._request('GET', endpoint,body);
    return data;
  }; 

  
}



const api_client = new ApiClient()

export default api_client;
