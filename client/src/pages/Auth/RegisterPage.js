import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Mobile } from "MediaQuery";
import { Box, TextField } from "@material-ui/core";
import useStyles from "styles/AuthPageStyle";
import Navbar from "components/common/Navbar";
import Toast from "components/common/Toast";
import Buttons from "components/common/Buttons";

function RegisterPage() {
  const classes = useStyles();
  const history = useHistory();
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [passwordCheck, setPasswordCheck] = useState("");
  const [name, setName] = useState("");
  const [blank, setBlank] = useState(false);
  const [toast, setToast] = useState(false);
  const [text, setText] = useState("");
  const [severity, setSeverity] = useState("");

  // (회원가입 폼) 입력 핸들러
  const onChangeHandler = (event) => {
    const {
      target: { name, value },
    } = event;

    if (name === "id") {
      setId(value);
    } else if (name === "password") {
      setPassword(value);
    } else if (name === "passwordCheck") {
      setPasswordCheck(value);
    } else if (name === "name") {
      setName(value);
    }
  };

  // validation 경고 문구
  const onToastHandler = (msg, svt) => {
    setText(msg);
    setSeverity(svt);
    setToast(true);
    window.setTimeout(() => {
      setToast(false);
    }, 3000);
  };

  // 회원가입 버튼 핸들러
  const onSignUpHandler = (event) => {
    event.preventDefault();
    if (!id || !password || !passwordCheck || !name) {
      setBlank(true);
    } else if (password === passwordCheck) {
      axios
        .post(`${process.env.REACT_APP_API_URL}/api/signup/`, {
          email: id,
          password: password,
          username: name,
          withCredentials: true,
        })
        .then((response) => {
          console.log(response);
          if (response.status === 201) {
            onToastHandler("회원가입 성공", "success");
            history.push({
              pathname: "/register/closet",
            });
            localStorage.setItem("jwt", response.data.token);
            localStorage.setItem("username", response.data.username);
            localStorage.setItem("email", response.data.email);
          } else {
            console.log(response.data);
          }
        })
        .catch((error) => {
          console.log(error.response);
          if (error.response.data.email) {
            onToastHandler(error.response.data.email[0], "error");
          } else if (error.response.data.password) {
            onToastHandler(error.response.data.password[0], "error");
          } else {
            onToastHandler("오류 발생", "warning");
          }
        })
        .then(
          axios
            .get(`${process.env.REACT_APP_API_URL}/api/current/`, {
              headers: { Authorization: "JWT " + localStorage.getItem("jwt") },
            })
            .then((response) => {
              localStorage.setItem("user", response.data.pk);
              localStorage.setItem("username", response.data.username);
              localStorage.setItem("email", response.data.email);
              localStorage.setItem("user", response.data.pk);
            }),
        );
    }
  };

  return (
    <Mobile>
      <Navbar />
      <Box className={classes.mobileAuthBox}>
        {toast ? <Toast text={text} severity={severity} /> : null}
        <form>
          <Box className={classes.mobileInputBox}>
            <TextField
              className={classes.mobileTextField}
              error={!id && blank ? true : false}
              id="standard-basic"
              label="아이디를 입력해주세요."
              name="id"
              type="text"
              value={id}
              onChange={onChangeHandler}
            />
            <TextField
              className={classes.mobileTextField}
              error={!password && blank ? true : false}
              id="standard-basic"
              label="비밀번호를 입력해주세요."
              name="password"
              type="password"
              value={password}
              onChange={onChangeHandler}
            />
            <TextField
              className={classes.mobileTextField}
              error={passwordCheck && password !== passwordCheck ? true : false}
              id="standard-basic"
              label={
                passwordCheck && password !== passwordCheck
                  ? "비밀번호가 일치하지 않습니다."
                  : "비밀번호를 확인해주세요."
              }
              name="passwordCheck"
              type="password"
              value={passwordCheck}
              onChange={onChangeHandler}
            />
            <TextField
              className={classes.mobileTextField}
              error={!name && blank ? true : false}
              id="standard-basic"
              label="이름을 입력해주세요."
              name="name"
              type="text"
              value={name}
              onChange={onChangeHandler}
            />
          </Box>
          <Box onClick={onSignUpHandler} className={classes.mobileButtonBox}>
            <Buttons className={classes.mobileButton} text="가입하기"></Buttons>
          </Box>
        </form>
      </Box>
    </Mobile>
  );
}

export default RegisterPage;
