import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Mobile } from "MediaQuery";
import { Box, TextField } from "@material-ui/core";
import useStyles from "styles/AuthPageStyle";
import Navbar from "components/common/Navbar";
import Buttons from "components/common/Buttons";
import Toast from "components/common/Toast";

import { useRecoilState, useRecoilValue } from "recoil";
import { idState, passwordState, toastState } from "state/State";
import Test from "utils/onChangeHandler";

function LoginPage() {
  const classes = useStyles();
  const history = useHistory();
  const [id, setId] = useRecoilState(idState);
  const [password, setPassword] = useRecoilState(passwordState);
  const [blank, setBlank] = useState(false);
  const toast = useRecoilValue(toastState);
  const [text, setText] = useState("실험중");
  const [severity, setSeverity] = useState("error");

  function ChangeHandler(event) {
    const {
      target: { name, value },
    } = event;

    if (name === "id") {
      setId(value);
    } else if (name === "password") {
      setPassword(value);
    }
  }

  // validation 경고 문구
  // const onToastHandler = (msg, svt) => {
  //   setText(msg);
  //   setSeverity(svt);
  //   setToast(true);
  //   window.setTimeout(() => {
  //     setToast(false);
  //   }, 3000);
  // };

  // 로그인 버튼 핸들러
  const onLoginHandler = (event) => {
    event.preventDefault();
    if (!id || !password) {
      setBlank(true);
    } else {
      axios
        .post(`${process.env.REACT_APP_API_URL}/api/login/`, {
          email: id,
          password: password,
          withCredentials: true,
        })
        .then((response) => {
          if (response.status === 200) {
            localStorage.setItem("jwt", response.data.token);
            // onToastHandler("로그인 성공!", "success");
            axios
              .get(`${process.env.REACT_APP_API_URL}/api/current/`, {
                headers: {
                  Authorization: "JWT " + localStorage.getItem("jwt"),
                },
              })
              .then((response) => {
                localStorage.setItem("username", response.data.username);
                localStorage.setItem("email", response.data.email);
                localStorage.setItem("user", response.data.pk);
              })
              .then(
                history.push({
                  pathname: "/mypage",
                }),
              );
          } else {
            alert("error");
          }
        })
        .catch((error) => {
          if (error.response.data.email) {
            // onToastHandler(error.response.data.email[0], "error");
          } else if (error.response.data.password) {
            // onToastHandler(error.response.data.password[0], "error");
          } else if (error.response.data.non_field_errors) {
            Test("으악");
            // onToastHandler("아이디 혹은 비밀번호를 확인해주세요.", "error");
          } else {
            console.log(error.response);
            // onToastHandler("예상치 못한 오류 발생", "error");
          }
        });
    }
  };

  return (
    <Mobile>
      <Navbar />
      <Box className={classes.mobileFullBox}>
        {toast ? <Toast text={text} severity={severity} /> : null}
        <Box className={classes.mobileGlassBox}>
          <Box className={classes.mobileAuthBox}>
            <form className={classes.mobileFormBox}>
              <Box className={classes.mobileInputBox}>
                <TextField
                  className={classes.mobileTextField}
                  error={!id && blank ? true : false}
                  id="standard-basic"
                  label="아이디를 입력해주세요."
                  name="id"
                  type="text"
                  value={id}
                  onChange={ChangeHandler}
                />
                <TextField
                  className={classes.mobileTextField}
                  error={!password && blank ? true : false}
                  id="standard-basic"
                  label="비밀번호를 입력해주세요."
                  name="password"
                  type="password"
                  value={password}
                  onChange={ChangeHandler}
                />
                <br />
              </Box>
              <Box className={classes.mobileButtonBox}>
                <Box onClick={onLoginHandler}>
                  <Buttons
                    className={classes.mobileButton}
                    variant="contained"
                    text="로그인"
                    url="/login"
                  />
                </Box>
                <Box className={classes.mobileLinkBox}>
                  <a href="/register">회원가입 하러가기</a>
                </Box>
              </Box>
            </form>
          </Box>
        </Box>
      </Box>
    </Mobile>
  );
}

export default LoginPage;
