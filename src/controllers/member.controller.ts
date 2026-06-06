import { Request, Response } from "express";
import { T } from "../libs/types/common";
import MemberService from "../models/Member.service";
import { Member, LoginInput, MemberInput } from "../libs/types/member";
import Errors from "../libs/Errors";

const memberService = new MemberService();
const memberController: T = {};


memberController.signup = async (req: Request, res: Response) => {
    try {
        console.log("signup");

        const input: MemberInput = req.body,
            result: Member = await memberService.signup(input);

        // TODO - TOKENS
        res.json({ member: result });
    } catch (err) {
        console.log("Error, signup:", err);
        if (err instanceof Errors) res.status(err.code).json(err);
        else res.status(Errors.standart.code).json(Errors.standart);
        // res.json({error: err});
    }

};

memberController.login = async (req: Request, res: Response) => {
    try {
        console.log("login");
        const input: LoginInput = req.body,
            result = await memberService.login(input);

        // TODO - TOKENS


        res.json({ member: result });
    } catch (err) {
        console.log("Error, login:", err);
        // res.json({error: err});
    }

};



export default memberController;