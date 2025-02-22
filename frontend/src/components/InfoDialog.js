import React, { Component } from 'react'
import { withTranslation, Trans} from "react-i18next";
import {Typography, Link, DialogActions,  DialogContent, Button, Grid} from "@mui/material"
import Image from 'material-ui-image'
import MediaQuery from 'react-responsive'

class InfoDialog extends Component {
  render() {
    const { t } = this.props;
    return (
      <div>
        <DialogContent>

          <MediaQuery minWidth={475}>
          <Grid container xs={12}>
            <Grid item xs={8}>
              <Typography component="h4" variant="h4">{t("What is RoboSats?")}</Typography>
              <Typography component="body2" variant="body2">
                <p>{t("It is a BTC/FIAT peer-to-peer exchange over lightning.")} <br/> 
                {t("It simplifies matchmaking and minimizes the need of trust. RoboSats focuses in privacy and speed.")}</p>
                
                <p>{t("RoboSats is an open source project ")} <Link 
                  href='https://github.com/reckless-satoshi/robosats'>{t("(GitHub).")}</Link>
                </p>
              </Typography>
            </Grid>
            <Grid item xs={4} align="center">
              <Image className='newAvatar'
                disableError='true'
                cover='true'
                color='null'
                src={window.location.origin +'/static/assets/images/v0.1.2-04.png'}
              />
            </Grid>
          </Grid>
          </MediaQuery>

          <MediaQuery maxWidth={474}>
          <Typography component="h4" variant="h4">{t("What is RoboSats?")}</Typography>
          <Typography component="body2" variant="body2">
            <p>{t("It is a BTC/FIAT peer-to-peer exchange over lightning.")+" "} {t("It simplifies matchmaking and minimizes the need of trust. RoboSats focuses in privacy and speed.")}</p>
              <img
                width='100%'
                src={window.location.origin +'/static/assets/images/v0.1.2-03.png'}
              />
            <p>{t("RoboSats is an open source project ")} <Link 
              href='https://github.com/reckless-satoshi/robosats'>{t("(GitHub).")}</Link>
            </p>
          </Typography>
          </MediaQuery>

          <Typography component="h5" variant="h5">{t("How does it work?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("AnonymousAlice01 wants to sell bitcoin. She posts a sell order. BafflingBob02 wants to buy bitcoin and he takes Alice's order. Both have to post a small bond using lightning to prove they are real robots. Then, Alice posts the trade collateral also using a lightning hold invoice. RoboSats locks the invoice until Alice confirms she received the fiat, then the satoshis are released to Bob. Enjoy your satoshis, Bob!")}</p>

            <p>{t("At no point, AnonymousAlice01 and BafflingBob02 have to entrust the bitcoin funds to each other. In case they have a conflict, RoboSats staff will help resolving the dispute.")} 
              {t("You can find a step-by-step description of the trade pipeline in ")}
              <Link href='https://github.com/Reckless-Satoshi/robosats/blob/main/README.md#how-it-works'>{t("How it works")}</Link>.
              {" "+t("You can also check the full guide in ")}
              <Link href='https://github.com/Reckless-Satoshi/robosats/blob/main/docs/how-to-use.md'>{t("How to use")}</Link>.</p>
          </Typography>

          <Typography component="h5" variant="h5">{t("What payment methods are accepted?")}</Typography>
          <Typography component="body2" variant="body2">
            <p>{t("All of them as long as they are fast. You can write down your preferred payment method(s). You will have to match with a peer who also accepts that method. The step to exchange fiat has a expiry time of 24 hours before a dispute is automatically open. We highly recommend using instant fiat payment rails.")} </p>
          </Typography>

          <Typography component="h5" variant="h5">{t("Are there trade limits?")}</Typography>
          <Typography component="body2" variant="body2">
            <p>{t("Maximum single trade size is {{maxAmount}} Satoshis to minimize lightning routing failure. There is no limits to the number of trades per day. A robot can only have one order at a time. However, you can use multiple robots simultaneously in different browsers (remember to back up your robot tokens!).", {maxAmount: '1,200,000'})} </p>
          </Typography>

          <Typography component="h5" variant="h5">{t("Is RoboSats private?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("RoboSats will never ask you for your name, country or ID. RoboSats does not custody your funds and does not care who you are. RoboSats does not collect or custody any personal data. For best anonymity use Tor Browser and access the .onion hidden service.")} </p>
            <p>{t("Your trading peer is the only one who can potentially guess anything about you. Keep your chat short and concise. Avoid providing non-essential information other than strictly necessary for the fiat payment.")} </p>
          </Typography>

          <Typography component="h5" variant="h5">{t("What are the risks?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("This is an experimental application, things could go wrong. Trade small amounts!")}</p>
            <p> {t("The seller faces the same charge-back risk as with any other peer-to-peer service. Paypal or credit cards are not recommended.")}</p>
          </Typography>

          <Typography component="h5" variant="h5">{t("What is the trust model?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("The buyer and the seller never have to trust each other. Some trust on RoboSats is needed since linking the seller's hold invoice and buyer payment is not atomic (yet). In addition, disputes are solved by the RoboSats staff.")}</p> 
            <p> {t("To be totally clear. Trust requirements are minimized. However, there is still one way RoboSats could run away with your satoshis: by not releasing the satoshis to the buyer. It could be argued that such move is not in RoboSats' interest as it would damage the reputation for a small payout. However, you should hesitate and only trade small quantities at a time. For large amounts use an onchain escrow service such as Bisq")}</p> 
            <p> {t("You can build more trust on RoboSats by inspecting the source code.")} <Link href='https://github.com/reckless-satoshi/robosats'> {t("Project source code")}</Link>. </p>
          </Typography>

          <Typography component="h5" variant="h5">{t("What happens if RoboSats suddenly disappears?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("Your sats will return to you. Any hold invoice that is not settled would be automatically returned even if RoboSats goes down forever. This is true for both, locked bonds and trading escrows. However, there is a small window between the seller confirms FIAT RECEIVED and the moment the buyer receives the satoshis when the funds could be permanently lost if RoboSats disappears. This window is about 1 second long. Make sure to have enough inbound liquidity to avoid routing failures. If you have any problem, reach out trough the RoboSats public channels.")}</p>
          </Typography>

          <Typography component="h5" variant="h5">{t("Is RoboSats legal in my country?")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("In many countries using RoboSats is no different than using Ebay or Craiglist. Your regulation may vary. It is your responsibility to comply.")}</p>
          </Typography>

          <Typography component="h5" variant="h5">{t("Disclaimer")}</Typography>
          <Typography component="body2" variant="body2">
            <p> {t("This lightning application is provided as is. It is in active development: trade with the utmost caution. There is no private support. Support is only offered via public channels ")}<Link href='https://t.me/robosats'>{t("(Telegram)")}</Link>{t(". RoboSats will never contact you. RoboSats will definitely never ask for your robot token.")}</p>
          </Typography>
          <DialogActions>
            <Button onClick={this.props.handleCloseInfo}>{t("Close")}</Button>
          </DialogActions>
        </DialogContent>
      </div>
    )
  }
}

export default withTranslation()(InfoDialog);