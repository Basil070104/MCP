import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

// Define our MCP agent with tools
export class MyMCP extends McpAgent {
	server = new McpServer({
		name: "WordWare MCP",
		version: "1.0.0",
	});

	API_URL = "http://127.0.0.1:8000/"

	async init() {
		// Simple addition tool
		this.server.tool(
			"add",
			{ a: z.number(), b: z.number() },
			async ({ a, b }) => ({
				content: [{ type: "text", text: String(a + b) }],
			})
		);

		// Calculator tool with multiple operations
		this.server.tool(
			"calculate",
			{
				operation: z.enum(["add", "subtract", "multiply", "divide"]),
				a: z.number(),
				b: z.number(),
			},
			async ({ operation, a, b }) => {
				let result: number;
				switch (operation) {
					case "add":
						result = a + b;
						break;
					case "subtract":
						result = a - b;
						break;
					case "multiply":
						result = a * b;
						break;
					case "divide":
						if (b === 0)
							return {
								content: [
									{
										type: "text",
										text: "Error: Cannot divide by zero",
									},
								],
							};
						result = a / b;
						break;
				}
				return { content: [{ type: "text", text: String(result) }] };
			}
		);

		this.server.tool(
			"research founder",
			{
				full_name: z.string().describe("The full name of the founder"),
				company: z.string().describe("The company that the founder works at"),
				website: z.string().describe("Url of the company that the person works")
			},
			async ({full_name, company, website}) => {
				try {
					// Call your API endpoint to get founders data
					const response = await fetch(`${this.API_URL}research_founders`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({ full_name, company, website })
					});

					if (!response.ok) {
						throw new Error(`API error: ${response.status}`);
					}
					
					const information: { message: string } = await response.json();

					return {
						content: [{ type: "text", text: information.message }]
					};
				} catch (error) {
					return {
						content: [{ 
							type: "text", 
							text: `Error finding founders. Please check the API connection.` 
						}]
					}
				}
			}
		)

		this.server.tool(
			"personalized questions",
			{
				full_name: z.string().describe("The full name of the founder"),
				company: z.string().describe("The company that the founder works at"),
				competiton: z.string().describe("This is the competition you are analyzing")
			},
			async ({full_name, company, competiton}) => {
				try {
					// Call your API endpoint to get founders data
					const response = await fetch(`${this.API_URL}personalized_questions`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({ full_name, company, competiton })
					});

					if (!response.ok) {
						throw new Error(`API error: ${response.status}`);
					}
					
					const information: { message: string } = await response.json();

					return {
						content: [{ type: "text", text: information.message }]
					};
				} catch (error) {
					return {
						content: [{ 
							type: "text", 
							text: `Error finding founders. Please check the API connection.` 
						}]
					}
				}
			}
		)

		this.server.tool(
			"personalized research",
			{
				full_name: z.string().describe("The full name of the founder"),
				company: z.string().describe("The company that the founder works at"),
				competiton: z.string().describe("This is the competition you are analyzing")
			},
			async ({full_name, company, competiton}) => {
				try {
					// Call your API endpoint to get founders data
					const response = await fetch(`${this.API_URL}personalized_questions`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({ full_name, company, competiton })
					});

					if (!response.ok) {
						throw new Error(`API error: ${response.status}`);
					}
					
					const information: { message: string } = await response.json();

					return {
						content: [{ type: "text", text: information.message }]
					};
				} catch (error) {
					return {
						content: [{ 
							type: "text", 
							text: `Error finding founders. Please check the API connection.` 
						}]
					}
				}
			}
		)

		this.server.tool(
			"enriching leaders",
			{
				full_name: z.string().describe("The full name of the founder"),
				company: z.string().describe("The company that the founder works at"),
				website: z.string().describe("Url of the company that the person works")
			},
			async ({full_name, company, website}) => {
				try {
					// Call your API endpoint to get founders data
					const response = await fetch(`${this.API_URL}enriching_leaders`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({ full_name, company, website })
					});

					if (!response.ok) {
						throw new Error(`API error: ${response.status}`);
					}
					
					const information: { message: string } = await response.json();
					return {
						content: [{ type: "text", text: information.message}]
					};
				} catch (error) {
					return {
						content: [{ 
							type: "text", 
							text: `Error finding founders. Please check the API connection.` 
						}]
					}
				}
			}
		)

		this.server.tool(
			"ReAct Agent",
			{
				question: z.string().describe("Any question that the user has."),

			},
			async ({question}) => {
				try {
					// Call your API endpoint to get founders data
					const response = await fetch(`${this.API_URL}react_agent`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({ question })
					});

					if (!response.ok) {
						throw new Error(`API error: ${response.status}`);
					}
					
					const information: { message: string } = await response.json();
					return {
						content: [{ type: "text", text: information.message}]
					};
				} catch (error) {
					return {
						content: [{ 
							type: "text", 
							text: `Error finding founders. Please check the API connection.` 
						}]
					}
				}
			}
		)

	}
}

export default {
	fetch(request: Request, env: Env, ctx: ExecutionContext) {
		const url = new URL(request.url);

		if (url.pathname === "/sse" || url.pathname === "/sse/message") {
			// @ts-ignore
			return MyMCP.serveSSE("/sse").fetch(request, env, ctx);
		}

		if (url.pathname === "/mcp") {
			// @ts-ignore
			return MyMCP.serve("/mcp").fetch(request, env, ctx);
		}

		return new Response("Not found", { status: 404 });
	},
};
