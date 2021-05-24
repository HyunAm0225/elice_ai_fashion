import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
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
    border: "1px solid var(--color-bg-dark)",
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
    borderTop: "1px solid var(--color-bg-dark)",
    paddingTop: "20px",
  },
  mobileSmallPadding: {
    padding: "10px",
  },
  mobileImage: {
    objectFit: "cover",
    height: "100%",
    width: "100%",
    borderRadius: "15px",
  },
  mobileShoppingBox: {
    paddingTop: "10px",
    borderTop: "1px solid var(--color-bg-dark)",
    height: "17vh",
    lineHeight: "5vh",
  },
  mobileInformationBox: {
    paddingTop: "10px",
    borderTop: "1px solid var(--color-bg-dark)",
    height: "22vh",
    lineHeight: "5vh",
  },
  mobileBoldText: {
    fontWeight: "bold",
  },
  mobileFooterBox: {
    textAlign: "center",
    paddingTop: "15px",
    height: "10vh",
    borderTop: "1px solid var(--color-bg-dark)",
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
