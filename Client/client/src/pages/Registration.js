import React, { useState } from "react";
import "../index.css";
import "../style.css";
import { Link } from "react-router-dom";
import httpClient from "./httpClient";

const Registration = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const User_Registration = async () => {
    console.log(email, password);

    try {
      const resp = await httpClient.post("//localhost:5000/register", {
        email,
        password,
      });
      window.location.href = "/";
    } catch (error) {
      if (error.response.status === 401) {
        alert("invalied Credential");
      }
    }
  };

  return (
    <div>
      <Link to="/" className="btn btn-light my-3 mx-5">
        Go Back
      </Link>
      <h3 className="center">Registration</h3>
      {/* Registration form */}

      <div className="container">
        <div className="forms">
          <div className="form signup">
            <span className="title">Registration</span>
            <form action="#">
              <div className="input-field">
                <input type="text" placeholder="Enter your name" required />
              </div>
              <div className="input-field">
                <input
                  type="text"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="input-field">
                <input
                  type="password"
                  className="password"
                  placeholder="Create a password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              <div className="input-field">
                <input
                  type="password"
                  className="password"
                  placeholder="Confirm a password"
                  required
                />
              </div>
              <div className="checkbox-text">
                <div className="checkbox-content">
                  <input type="checkbox" id="sigCheck" />
                  <label htmlFor="sigCheck" className="text">
                    Remember me
                  </label>
                </div>
                <a href="" className="text">
                  Forgot password?
                </a>
              </div>
              <div className="input-field button">
                <input
                  type="button"
                  defaultValue="Login Now"
                  onClick={() => User_Registration()}
                />
              </div>
            </form>
            <div className="login-signup">
              <span className="text">
                Not a member?
                <a href="login" className="text login-link">
                  Signup now
                </a>
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Registration form */}
    </div>
  );
};

export default Registration;
