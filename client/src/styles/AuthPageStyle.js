import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  // Auth 공통
  mobileAuthBox: {
    height: "91vh",
    width: "100%",
    display: "flex",
    justifyContent: "center",
  },
  mobileInputBox: {
    height: "63.9vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },

  mobileTextField: {
    margin: "0.5vw",
  },
  mobileButtonBox: {
    height: "26.1vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },
  mobileButton: {
    width: "70vw",
    borderRadius: "15px",
  },

  // RegisterClosetPage
  mobileTextBox: {
    height: "63.9vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  mobileControlBox: {
    height: "10vh",
  },
  mobileMessage: {
    width: "70vw",
  },
}));

export default useStyles;
