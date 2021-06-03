import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({

  mobileItemMainGrid:{
    margin: "25px",
    textAlign:"center",
    padding: "30px",
    backgroundColor:"black"
  },

  mobileWelcomeBox: {
    height: "6vh",
    marginBottom: "3vh",
    display: "flex",
    justifyContent: "space-between",
  },
  mobileWelcomeText: {
    lineHeight: "6vh",
    fontSize: "18px",
    fontWeight: "bold",
  },
  mobileCategoryButton: {
    borderRadius: "15px",
    margin: "5px",
    backgroundColor: "var(--color-bg-dark)",
    fontWeight: "700",
    fontSize: "14px",
    paddingTop: "2px",
    paddingBottom: "2px",
    "&:hover, &:focus, &:active": {
      backgroundColor: "var(--color-main-b)",
      color: "var(--color-main-c)",
    },
  },
  mobileStyleBookBox: {
    height: "27vh",
    position: "relative",
  },
  mobileStyleBookText: {
    fontWeight: "bold",
    fontSize: "18px",
    zIndex: "100",
    position: "absolute",
    top: "-10px",
    background: "white",
    paddingRight: "10px",
  },
  mobileStyleImageBox: {
    height: "90%",
    paddingTop: "20px",
  },
  mobileShoppingBox: {
    paddingTop: "10px",
    height: "17vh",
    lineHeight: "5vh",
  },
  mobileShoppingText: {
    display: "block",
    textDecoration: "none",
    color: "var(--color-gray)",
  },
  mobileInformationBox: {
    paddingTop: "10px",
    height: "22vh",
    lineHeight: "5vh",
  },
  mobileInfomationText: {
    display: "block",
    textDecoration: "none",
    color: "var(--color-gray)",
  },
  mobileFooterBox: {
    textAlign: "center",
    paddingTop: "15px",
    height: "10vh",
  },
  mobileFooterText: {
    width: "75vw",
    display: "inline-block",
    fontSize: "11px",
    fontWeight: "lighter",
    color: "var(--color-gray)",
  },
}));

export default useStyles;
